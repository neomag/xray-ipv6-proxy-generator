import ipaddress
import random
import os
from dotenv import load_dotenv

load_dotenv()
IPV6_SUBNET = os.getenv('IPV6_SUBNET')
MAX_IPS = int(os.getenv('MAX_IPS'))
INTERFACE = os.getenv('INTERFACE')
ADDRESS_FILE = os.getenv('ADDRESS_FILE')

print(f'IPV6_SUBNET = {IPV6_SUBNET}')
print(f'MAX_IPS = {MAX_IPS}')
print(f'INTERFACE = {INTERFACE}')
print(f'ADDRESS_FILE = {ADDRESS_FILE}')


subnet = IPV6_SUBNET
num_addresses = MAX_IPS
filename = ADDRESS_FILE

def generate_random_ipv6_in_subnet(subnet, num_addresses):
    subnet = ipaddress.IPv6Network(subnet)
    if subnet.prefixlen > 48:
        raise ValueError("Subnet must be at least /48")
    
    addresses = []
    for _ in range(num_addresses):
        # Генерируем случайные 80 бит для части адреса после префикса /48
        random_suffix = random.getrandbits(128 - subnet.prefixlen)
        # Создаем полный адрес, добавляя случайные биты к префиксу подсети
        address = subnet.network_address + random_suffix
        addresses.append(str(address))
    
    return addresses

def save_addresses_to_file(addresses, filename):
    with open(filename, 'w') as file:
        for address in addresses:
            file.write(address + '\n')

def check_addresses_in_subnet(addresses, subnet):
    subnet = ipaddress.IPv6Network(subnet)
    for address in addresses:
        ip = ipaddress.IPv6Address(address)
        if ip not in subnet:
            print(f"Address {address} is not in the subnet !!! {subnet}")
            exit(1)
            return False
    return True



addresses = generate_random_ipv6_in_subnet(subnet, num_addresses)

# Проверка принадлежности адресов подсети
if check_addresses_in_subnet(addresses, subnet):
    save_addresses_to_file(addresses, filename)
    print(f"{num_addresses} случайных IPv6-адресов сохранены в файл {filename}")
else:
    print("Некоторые адреса не принадлежат указанной подсети.")
