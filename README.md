# WB_Net_Config

WB_Net_Config is a tool for configuration network of ubuntu 18 

## Install Dependency

pip install flask
pip install pyyaml
pip install netifaces

## How to use
Step 1: Modify the config in config.py file to match with your device:

config = { 
                "if_name": "eno1", 
                "sudo_pass": 'cutetrang', 
                "netplan_file_config_path":"/etc/netplan/01-network-manager-all.yaml" 
         }
with if_name is ethernet interface name 
sudo_pass is pass woed of root account
netplan_file_config_path is path to netplan config 

Step 2: change mode of netplan config file to mode w/r by command
sudo chmode 777 /etc/netplan/01-network-manager-all.yaml

Step 3: copy content of 01-network-manager-all.yaml in this repo and replace content in /etc/netplan/01-network-manager-all.yamlfile

Step 4: Run python app.py than config the IP on the WB
