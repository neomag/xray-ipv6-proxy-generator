def run():
  import json
  import os
  from dotenv import load_dotenv


  PROXY_USER = os.getenv('PROXY_USER')
  PROXY_PASS = os.getenv('PROXY_PASS')
  
  print(f"PROXY_USER={PROXY_USER}")
  print(f"PROXY_PASS={PROXY_PASS}")
   
  with open('config.example.json') as file:
      file_contents = file.read()
      config = json.loads(file_contents)

  with open('address.txt') as file:
      addresses = file.read().splitlines()


  data = config['inbounds']


  for addr in addresses:
      new_inbound = f"""
      {{
        "listen": "{addr}",
        "port": 8080,
        "protocol": "http",
        "settings": {{
          "accounts": [
            {{
              "user": "{PROXY_USER}",
              "pass": "{PROXY_PASS}"
            }}
          ]
        }},
        "streamSettings": null,
        "tag": "inbound-{addr}:8080",
        "sniffing": {{
          "enabled": false,
          "destOverride": [
            "http",
            "tls",
            "quic",
            "fakedns"
          ],
          "metadataOnly": false,
          "routeOnly": false
        }}
      }}
      """
      new_inbound_dict = json.loads(new_inbound) 
      data.append(new_inbound_dict)

  config['inbounds'] = data
  with open("inbound.json", "w") as json_file:
          json.dump(config, json_file, indent=4)

  print('inbound.json generated...')