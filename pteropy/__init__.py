import requests
import os
import json


class Pterodactyl_Application:
    def __init__(self, base_url, api_key):
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key

    def check(self):
        endpoint = f"{self.base_url}/api/application/users"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "Application/vnd.pterodactyl.v1+json"
        }
        try:
            response = requests.get(endpoint, headers=headers)
        except:

            return False
        try:
            response.json()["errors"]
            return False
        except:
            return True

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

    def load_egg(self, f: str):
        all = os.listdir(f)
        for i in all:
            if i[-5:] == ".json":
                with open(f"{f}/{i}", mode="r", encoding="utf-8") as filt:
                    data = json.load(filt)
                print(data["name"])


class Pterodactyl_Client:
    def __init__(self, base_url, api_key):
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key

    def check(self):
        endpoint = f"{self.base_url}/api/client/account"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "Application/vnd.pterodactyl.v1+json"
        }
        try:
            response = requests.get(endpoint, headers=headers)
        except:

            return False
        try:
            response.json()["errors"]
            return False
        except:
            return True

    def list_servers(self):
        url = f'{self.base_url}/api/client'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def account_details(self):
        url = f'{self.base_url}/api/client/account'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def details_2FA(self):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def enable_2FA(self, code):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = '{"code": "awa"}'.replace("awa", code)

        response = requests.request('POST', url, data=payload, headers=headers)
        return response.json()

    def disable_2FA(self, password):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = '{"password": "pd"}'.replace("pd", password)

        response = requests.request(
            'DELETE', url, data=payload, headers=headers)
        return response

    def update_email(self, email, password):
        url = f'{self.base_url}/api/client/account/email'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = '{"email": "ema","password": "pd"}'.replace(
            "ema", email).replace("pd", password)

        response = requests.request('PUT', url, data=payload, headers=headers)
        return response

    def update_password(self, current_password, new_password):
        url = f'{self.base_url}/api/client/account/password'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = '{"current_password": "Pd","password": "pd","password_confirmation": "pd"}'.replace(
            "Pd", current_password).replace("pd", new_password)

        response = requests.request('PUT', url, data=payload, headers=headers)
        return response

    def list_API_keys(self):
        url = f'{self.base_url}/api/client/account/api-keys'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def create_API_key(self, description, allowed_ips: list = None):
        url = f'{self.base_url}/api/client/account/api-keys'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if allowed_ips == None:
            payload = '{"description": "dn"}'.replace("dn", description)
        else:
            payload = '{"description": "Restricted IPs","allowed_ips": []}'.replace(
                "dn", description).replace("[]", allowed_ips)

        response = requests.request('POST', url, data=payload, headers=headers)
        return response.json()

    def delete_API_key(self, key_identifier):
        url = f'{self.base_url}/api/client/account/api-keys/{key_identifier}'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        response = requests.request('DELETE', url,  headers=headers)
        return response

    def get_server(self, server: str):
        self.server = server
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

    def stop_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"signal": "stop"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def start_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"signal": "start"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def restart_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"signal": "restart"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def kill_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"signal": "kill"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def rename_server(self, server: str, name: str):
        url = f'{self.base_url}/api/client/servers/{server}/settings/rename'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"name": "awa"}'.replace("awa", name)
        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def send_command(self, server: str, command: str):
        url = f'{self.base_url}/api/client/servers/{server}/command'
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = '{"command": "awa"}'.replace("awa", command)
        response = requests.request('POST', url, data=payload, headers=headers)
        return response
