
import os
from dotenv import load_dotenv
import inbound
import outbound
import routing
import mubeng

print("checking required files...")

files_to_check = [".env", "address.txt", "config.example.json"]

load_dotenv()

def check_files_exist(files):
    for file in files:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"file {file} does not exists!")
            exit()
    print(f"{files_to_check} found...")

try:
    check_files_exist(files_to_check)
except FileNotFoundError as e:
    print(e)



inbound.run()
outbound.run()
routing.run()
mubeng.run()