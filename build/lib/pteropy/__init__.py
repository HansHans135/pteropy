import requests
import os
import json
class Pterodactyl_Application:
    def __init__(self, base_url, api_key):
        print("pteropy setting...")
        if base_url[-1]=="/":
            base_url=base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key
        endpoint = f"{self.base_url}/api/application/users"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "Application/vnd.pterodactyl.v1+json"
        }
        try:
            response = requests.get(endpoint, headers=headers)
        except:
            print("Pterodactyl panel url invalid :(")
            return
        try:
            response.json()["errors"]
            print("Pterodactyl token invalid :(")
        except:
            print("pteropy ready!")
        #print(response.json())
    def list_uesrs(self):
        url = f'{self.base_url}/api/application/users'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

        response = requests.request('GET', url, headers=headers)
        return response.json()
    
    def create_user(self, username, email, password):
        endpoint = f"{self.base_url}/api/application/users"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "Application/vnd.pterodactyl.v1+json"
        }
        data = {
            "username": username,
            "first_name": username,
            "last_name": username,
            "email": email,
            "password": password
        }
        response = requests.post(endpoint, headers=headers, json=data)
        return response.json()
    def load_egg(self ,f:str):
        all = os.listdir(f)
        for i in all:
            if i[-5:] == ".json":
                with open(f"{f}/{i}", mode="r", encoding="utf-8") as filt:
                    data = json.load(filt)
                print(data["name"])


class Pterodactyl_Client:
    def __init__(self, base_url, api_key):
        print("pteropy setting...")
        if base_url[-1]=="/":
            base_url=base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key
        endpoint = f"{self.base_url}/api/client/account"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "Application/vnd.pterodactyl.v1+json"
        }
        try:
            response = requests.get(endpoint, headers=headers)
        except:
            print("Pterodactyl panel url invalid :(")
            return
        try:
            response.json()["errors"]
            print("Pterodactyl token invalid :(")
        except:
            print("pteropy ready!")
    
    def list_servers(self):
        url = f'{self.base_url}/api/client'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json"
    }

        response = requests.request('GET', url, headers=headers)
        return response.json()
    
    def get_server(self,server:str):
        self.server=server
        url = f'{self.base_url}/api/client/servers/{self.server}'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

        response = requests.request('GET', url, headers=headers)
        try:
            if response.json()["errors"][0]["status"] == "404":
                return None
            else:
                return response.json()
        except:
            return response.json()
    
    def stop_server(self,server:str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
        payload = '{"signal": "stop"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response
    
    def start_server(self,server:str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
        payload = '{"signal": "start"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response
    
    def restart_server(self,server:str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
        payload = '{"signal": "restart"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response
    
    def kill_server(self,server:str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
        payload = '{"signal": "kill"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response
    
    def rename_server(self,server:str,name:str):
        url = f'{self.base_url}/api/client/servers/{server}/settings/rename'
        headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
        payload = {
            "name": name
        }
        response = requests.request('POST',url,data=payload,headers=headers)
        return response
        
    def send_command(self,server:str,command:str):
        url = f'{self.base_url}/api/client/servers/{server}/command'
        headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
        payload = {
        "command": command
        }  
        response = requests.request('POST',url,data=payload,headers=headers)
        return response
