def run():
    import os
    from dotenv import load_dotenv

    PROXY_USER = os.getenv('PROXY_USER')
    PROXY_PASS = os.getenv('PROXY_PASS')

    with open('address.txt') as file:
        addresses = file.read().splitlines()


    proxies = []
    for addr in addresses:
        new_proxy = f"http://{PROXY_USER}:{PROXY_PASS}@{addr}:8080"
        proxies.append(new_proxy)


    file = open('proxies.txt', 'w')
    file.writelines(f"{line}\n" for line in proxies)
    file.close()

    print('proxies.txt generated...')