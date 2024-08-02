def run():
    import json
    import os

    with open('outbound.json') as file:
        file_contents = file.read()
        config = json.loads(file_contents)

    with open('address.txt') as file:
        addresses = file.read().splitlines()


    data = config['routing']['rules']


    for addr in addresses:
        new_rule = f"""
        {{
            "type": "field",
            "inboundTag": [
                "inbound-{addr}:8080"
            ],
            "outboundTag": "inbound-{addr}:8080"
        }}
        """
        new_rules_dict = json.loads(new_rule) 
        data.append(new_rules_dict)

    config['routing']['rules'] = data
    with open("routing.json", "w") as json_file:
            json.dump(config, json_file, indent=4)

    print('routing.json generated...')
    os.popen('cp routing.json config.json')
    print('copy routing.json to resulting config.json...')
