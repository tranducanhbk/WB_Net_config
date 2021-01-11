Installation:
flask,
yaml


## Quick Start
step 1: verify th ethernet_interface of netwok need to config by command:
ifconfig -a
output example:
br-fef35d53f4b4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
        inet6 fe80::42:e0ff:fe60:78c5  prefixlen 64  scopeid 0x20<link>
        ether 02:42:e0:60:78:c5  txqueuelen 0  (Ethernet)
        RX packets 2532  bytes 931282 (931.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3657  bytes 571525 (571.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:1aff:fe3d:2b86  prefixlen 64  scopeid 0x20<link>
        ether 02:42:1a:3d:2b:86  txqueuelen 0  (Ethernet)
        RX packets 13558  bytes 696949 (696.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 13627  bytes 6757181 (6.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.10  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::aaa1:59ff:fe06:bf59  prefixlen 64  scopeid 0x20<link>
        inet6 2402:800:6105:29d:aaa1:59ff:fe06:bf59  prefixlen 64  scopeid 0x0<global>
        inet6 2402:800:6105:29d::4  prefixlen 128  scopeid 0x0<global>
        ether a8:a1:59:06:bf:59  txqueuelen 1000  (Ethernet)
        RX packets 6886608  bytes 8752378743 (8.7 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4259713  bytes 495111714 (495.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xa4400000-a4420000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 10517199  bytes 62846036040 (62.8 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10517199  bytes 62846036040 (62.8 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth28f01c8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f09c:54ff:fe0d:8360  prefixlen 64  scopeid 0x20<link>
        ether f2:9c:54:0d:83:60  txqueuelen 0  (Ethernet)
        RX packets 2609  bytes 974470 (974.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3749  bytes 600465 (600.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth47c81b3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f0eb:48ff:fe47:3758  prefixlen 64  scopeid 0x20<link>
        ether f2:eb:48:47:37:58  txqueuelen 0  (Ethernet)
        RX packets 13558  bytes 886761 (886.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 13683  bytes 6763081 (6.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vetha4530f4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6ccc:deff:fece:c31f  prefixlen 64  scopeid 0x20<link>
        ether 6e:cc:de:ce:c3:1f  txqueuelen 0  (Ethernet)
        RX packets 47  bytes 24002 (24.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 233  bytes 24041 (24.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 
        
step 2: modify config.py

config = {
    "if_name": "eno1",
    "sudo_pass": 'cutetrang',
    "netplan_file_config_path":"/etc/netplan/01-network-manager-all.yaml"
}
with if_name is name interface
sudo_pass: is password for sudo account of linux
net_plan_file_config_path: is path to the network config yaml file 

step 3: change mode r/w for file 01-network-manager-all.yaml by command
sudo chmode 777  01-network-manager-all.yaml by comman


