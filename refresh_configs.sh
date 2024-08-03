#падать если exit code non zero
set -eou pipefail

cd /opt/proxies/utils/xray_config_generator

echo "saving old /opt/proxies/address.txt to ./address.txt.old"
cp -f /opt/proxies/address.txt ./address.txt.old


echo "generating ipv6..."
python3 generate_addresses.py


echo "add ipv6 on net interface..."
#python3 add_addresses.py
python3 add_addresses_v2.py
reset 2>&1 > /dev/null

echo "generating new configs for mubeng and xray..."
python3 main.py


echo "stopping mubeng and xray..."
systemctl stop mubeng.service
systemctl stop xray.service

echo "deleting ipv6..."
get_curr_ipv6 > address_curr.txt
python3 delete_addresses_v2.py
reset 2>&1 > /dev/null


echo "copy new configs proxies.txt and address.txt to /opt/proxies/"
cp -f ./proxies.txt /opt/proxies/proxies.txt
cp -f ./address.txt /opt/proxies/address.txt
cp -f ./config.json /opt/proxies/xray/config.json


echo "starting mubeng and xray..."
systemctl start mubeng.service
systemctl start xray.service
