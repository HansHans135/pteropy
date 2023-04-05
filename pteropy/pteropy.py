import requests

class Pterodactyl_Application:
    def __init__(self, base_url, api_key):
        print("Pterodactyl_Application setting...")
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
            print("Pterodactyl_Application panel url invalid :(")
            return
        try:
            response.json()["errors"]
            print("Pterodactyl_Application token invalid :(")
        except:
            print("Pterodactyl_Application ready!")
        #print(response.json())
    
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
