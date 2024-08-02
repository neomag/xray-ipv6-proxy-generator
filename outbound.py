def run():
    import json

    with open('inbound.json') as file:
        file_contents = file.read()
        config = json.loads(file_contents)

    with open('address.txt') as file:
        addresses = file.read().splitlines()


    data = config['outbounds']


    for addr in addresses:
        new_outbound = f"""
        {{
        "tag": "inbound-{addr}:8080",
        "protocol": "freedom",
        "settings": {{}},
        "sendThrough": "{addr}"
        }}
        """
        new_outbound_dict = json.loads(new_outbound) 
        data.append(new_outbound_dict)

    config['outbounds'] = data
    with open("outbound.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

    print('outbound.json generated...')