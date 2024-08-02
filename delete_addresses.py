import os
from dotenv import load_dotenv

def remove_ipv6_address(interface, address):
    try:
        command = f'sudo ip -6 addr del {address} dev {interface}'
        result = os.system(command)
        if result == 0:
            print(f"Successfully removed {address} from {interface}")
        else:
            print(f"Failed to remove {address} from {interface}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    load_dotenv()
    IPV6_SUBNET = os.getenv('IPV6_SUBNET')
    MAX_IPS = os.getenv('MAX_IPS')
    INTERFACE = os.getenv('INTERFACE')
    ADDRESS_FILE = os.getenv('ADDRESS_FILE')

    print(f'IPV6_SUBNET = {IPV6_SUBNET}')
    print(f'MAX_IPS = {MAX_IPS}')
    print(f'INTERFACE = {INTERFACE}')
    print(f'ADDRESS_FILE_PATH = {ADDRESS_FILE}')
    interface = INTERFACE
    addresses_file = ADDRESS_FILE
    
    try:
        with open(addresses_file, 'r') as file:
            addresses = file.readlines()
            
        for address in addresses:
            address = address.strip()
            if address:  # Ensure the address is not empty
                remove_ipv6_address(interface, address)
                
    except FileNotFoundError:
        print(f"File {addresses_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
