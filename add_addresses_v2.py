import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

def add_ipv6_address(interface, address):
    try:
        command = f'sudo ip -6 addr add {address} dev {interface}'
        result = os.system(command)
        if result == 0:
            #print(f"Successfully added {address} to {interface}")
            pass
        else:
            print(f"Failed to add {address} to {interface}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    load_dotenv()
    IPV6_SUBNET = os.getenv('IPV6_SUBNET')
    MAX_IPS = os.getenv('MAX_IPS')
    INTERFACE = os.getenv('INTERFACE')
    ADDRESS_FILE = os.getenv('ADDRESS_FILE')
    PARALLELISM = int(os.getenv('PARALLELISM', 1))  # Default to 1 thread if not set

    print(f'IPV6_SUBNET = {IPV6_SUBNET}')
    print(f'MAX_IPS = {MAX_IPS}')
    print(f'INTERFACE = {INTERFACE}')
    print(f'ADDRESS_FILE = {ADDRESS_FILE}')
    print(f'PARALLELISM = {PARALLELISM}')
    
    interface = INTERFACE
    addresses_file = ADDRESS_FILE
    
    try:
        with open(addresses_file, 'r') as file:
            addresses = [address.strip() for address in file.readlines() if address.strip()]
            
        with ThreadPoolExecutor(max_workers=PARALLELISM) as executor:
            future_to_address = {executor.submit(add_ipv6_address, interface, address): address for address in addresses}
            
            for future in as_completed(future_to_address):
                address = future_to_address[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"An error occurred while processing {address}: {e}")
                
    except FileNotFoundError:
        print(f"File {addresses_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
