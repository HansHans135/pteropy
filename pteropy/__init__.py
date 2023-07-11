import requests
import os
import json
import urllib.parse


class Pterodactyl_Application:
    def __init__(self, base_url, api_key):
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def check(self):
        endpoint = f"{self.base_url}/api/application/users"
        headers = self.headers
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
        headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def create_user(self, username, email, password):
        endpoint = f"{self.base_url}/api/application/users"
        headers = self.headers
        data = {
            "username": username,
            "first_name": username,
            "last_name": username,
            "email": email,
            "password": password
        }
        response = requests.post(endpoint, headers=headers, json=data)
        return response.json()


class Pterodactyl_Client:
    def __init__(self, base_url, api_key):
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def check(self):
        endpoint = f"{self.base_url}/api/client/account"
        headers = self.headers
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
        headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def account_details(self):
        url = f'{self.base_url}/api/client/account'
        headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def details_2FA(self):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def enable_2FA(self, code):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = self.headers
        payload = {"code": code}

        response = requests.request(
            'POST', url, data=json.dumps(payload), headers=headers)
        return response.json()

    def disable_2FA(self, password):
        url = f'{self.base_url}/api/client/account/two-factor'
        headers = self.headers
        payload = {"password": password}

        response = requests.request(
            'DELETE', url, data=json.dumps(payload), headers=headers)
        return response

    def update_email(self, email, password):
        url = f'{self.base_url}/api/client/account/email'
        headers = self.headers
        payload = {"email": email, "password": password}

        response = requests.request(
            'PUT', url, data=json.dumps(payload), headers=headers)
        return response

    def update_password(self, current_password, new_password):
        url = f'{self.base_url}/api/client/account/password'
        headers = self.headers
        payload = {"current_password": current_password,
                   "password": new_password, "password_confirmation": new_password}
        response = requests.request(
            'PUT', url, data=json.dumps(payload), headers=headers)
        return response

    def list_API_keys(self):
        url = f'{self.base_url}/api/client/account/api-keys'
        headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return response.json()

    def create_API_key(self, description, allowed_ips: list = None):
        url = f'{self.base_url}/api/client/account/api-keys'
        headers = self.headers
        if allowed_ips == None:
            payload = {"description": description}
        else:
            payload = {"description": description, "allowed_ips": allowed_ips}

        response = requests.request(
            'POST', url, data=json.dumps(payload), headers=headers)
        return response.json()

    def delete_API_key(self, key_identifier):
        url = f'{self.base_url}/api/client/account/api-keys/{key_identifier}'
        headers = self.headers
        response = requests.request('DELETE', url,  headers=headers)
        return response

    def list_databases(self, server):
        url = f'{self.base_url}/api/client/servers/{server}/databases'
        headers = self.headers
        response = requests.request('GET', url,  headers=headers)
        return response.json()

    def create_databases(self, server, database, remote):
        url = f'{self.base_url}/api/client/servers/{server}/databases'
        headers = self.headers
        payload = {
            "database": database,
            "remote": remote
        }
        response = requests.request(
            'POST', url, data=json.dumps(payload), headers=headers)
        return response.json()

    def rotate_password(self, server, database):
        url = f'{self.base_url}/api/client/servers/1a7ce997/databases/{database}/rotate-password'
        headers = self.headers
        response = requests.request('POST', url, headers=headers)
        return response.json()

    def delete_database(self, server, database):
        url = f'{self.base_url}/api/client/servers/{server}/databases/{database}'
        headers = self.headers
        response = requests.request('DELETE', url, headers=headers)
        return response

    def list_files(self, server, directory=None):
        if directory:
            url = f'{self.base_url}/api/client/servers/{server}/files/list?directory={urllib.parse.quote_plus(directory)}'
        else:
            url = f'{self.base_url}/api/client/servers/{server}/files/list'
        headers = self.headers
        response = requests.request('GET', url, headers=headers)
        return response.json()

    def get_file_contents(self, server, file):
        url = f'{self.base_url}/api/client/servers/{server}/files/contents?file={urllib.parse.quote_plus(file)}'
        headers = self.headers
        response = requests.request('GET', url,  headers=headers)
        return response.text

    def download_file(self, server, file):
        url = f'{self.base_url}/api/client/servers/{server}/files/download?file={urllib.parse.quote_plus(file)}'
        headers = self.headers
        response = requests.request('GET', url, headers=headers)
        return response.json()

    def rename_file(self, server,root,files):
        url = f'{self.base_url}/api/client/servers/{server}/files/rename'
        headers = self.headers
        payload = {
            "root": root,
            "files":files
        }

        response = requests.request('PUT', url, data=json.dumps(payload), headers=headers)
        return response

    def get_server(self, server: str):
        self.server = server
        url = f'{self.base_url}/api/client/servers/{self.server}'
        headers = self.headers

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
        headers = self.headers
        payload = '{"signal": "stop"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def start_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = self.headers
        payload = '{"signal": "start"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def restart_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = self.headers
        payload = '{"signal": "restart"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def kill_server(self, server: str):
        url = f'{self.base_url}/api/client/servers/{server}/power'
        headers = self.headers
        payload = '{"signal": "kill"}'

        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def rename_server(self, server: str, name: str):
        url = f'{self.base_url}/api/client/servers/{server}/settings/rename'
        headers = self.headers
        payload = {"name": name}
        response = requests.request(
            'POST', url, data=json.dumps(payload), headers=headers)
        return response

    def send_command(self, server: str, command: str):
        url = f'{self.base_url}/api/client/servers/{server}/command'
        headers = self.headers
        payload = {"command": command}
        response = requests.request(
            'POST', url, data=json.dumps(payload), headers=headers)
        return response
