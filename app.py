from flask import Flask, render_template, request
import netifaces
import os
import subprocess
import yaml
import time
from config import config


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
 

@app.route('/')
def index():
    return render_template('index.html',dhcp=1)


@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        if request.form.get('Save') == 'Save':
            network_set(request.form,config["if_name"])
            net_info = get_network_information(config["if_name"])
            time.sleep(1)
            dns = request.form["DNS"]
            dhcp = 1 if request.form["dhcp"] =="1" else 0
            dns_status = get_dns_status(config["if_name"])
            return render_template("index.html", net_info=net_info, dns=dns, dhcp=dhcp, dns_status=dns_status)

        elif request.form.get('Reload') == 'Reload': 
            net_info = get_network_information(config["if_name"])
            dns = get_dns(config["if_name"])
            dhcp = get_dhcp_status()
            dns_status = get_dns_status(config["if_name"])  
            return render_template("index.html", net_info=net_info, dns=dns, dhcp=dhcp, dns_status=dns_status)

        elif request.form.get('network_restart') == 'network_restart':
            f = os.popen('sudo netplan apply && echo '+ config["sudo_pass"])
            net_info = get_network_information(config["if_name"])
            dns = get_dns(config["if_name"])
            dhcp = get_dhcp_status()
            dns_status = get_dns_status(config["if_name"])
            return render_template("index.html",net_info=net_info, dns=dns, dhcp=dhcp, dns_status=dns_status) 
        elif request.form.get('delete') == 'delete':
            print("Delete click")
            dhcp = get_dhcp_status()
            return render_template("index.html", dhcp=dhcp)
    else:
    	return render_template("index.html",net_info=net_info, dns=dns, dhcp=dhcp) 

def get_data_from_yaml():
    with open(config["netplan_file_config_path"]) as file:
        data = yaml.full_load(file)
        file.close()  
    return data
    
data = get_data_from_yaml()

def network_set(info, if_name):
    dns = info['DNS'].split(',')
    for i in range(len(dns)):
        dns[i]= dns[i].strip() 
    if len(dns[0]) == 0:
        # if info['dhcp'] == "1":
        dns = []
        # else:
        #     dns=["8.8.8.8"]
    data['network']['ethernets'][if_name]['nameservers']['addresses']=dns

    if "checkbox_DNS" in info:
        data['network']['ethernets'][if_name]['dhcp4-overrides']["use-dns"] = True
    else:
        data['network']['ethernets'][if_name]['dhcp4-overrides']["use-dns"] = False

    if info['dhcp']=="1":
        data['network']['ethernets'][if_name]['dhcp4'] = True
        data['network']['renderer'] = "networkd" 
    else:
        data['network']['ethernets'][if_name]['dhcp4'] = False
        data['network']['ethernets'][if_name]['addresses'] = [info['Address']+'/24']
        data['network']['ethernets'][if_name]['gateway4'] = info['Gateway']
        data['network']['renderer'] = "networkd" 
    

    with open(config["netplan_file_config_path"], "w") as file:
        documents = yaml.dump(data, file, sort_keys=False )
        file.close()
    command = 'sudo netplan apply && echo ' + config["sudo_pass"]
    f = os.popen(command)

def get_dns_status(if_name):
    if data['network']['ethernets'][if_name]['dhcp4-overrides']['use-dns']==True:
        return 1
    else:
        return 0

def get_dns(if_name):
    dns =""
    f = os.popen('systemd-resolve --status')
    s = f.read().replace(" ","").split("("+if_name+")")	
    s1 = s[1].split("DNSServers:")
    try:
        s2 = s1[1].split("\r\n")
    except:
        return dns
    s3 = s2[0].strip().split("\n")
    for i in range(len(s3)):
        if s3[i].find("::")<0:
            dns+=s3[i]+ ",\xa0"
    return dns[:-2]
    
def get_network_information(if_name):
    PROTO = netifaces.AF_INET   # We want only IPv4, for now at least

    print(netifaces.interfaces())
    # Get addresses for each interface
    try:
        if_addrs = netifaces.ifaddresses(if_name)
    except:
        print('wrong interface')
        return -1
    add =  if_addrs[PROTO][0]['addr']
    netmask = if_addrs[PROTO][0]['netmask'] 
    gws = netifaces.gateways()['default'][netifaces.AF_INET][0]
        
    return (add, netmask, gws)

def get_dhcp_status():
    f= os.popen('ip r | grep default').read()
    if f.find("dhcp") >1:
        return 1
    else:
        return 0
    


if __name__ == '__main__':
    app.run()
