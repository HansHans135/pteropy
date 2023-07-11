# pteropy
適用於Pterodactyl api的python庫

# 安裝
```
pip install pteropy
```


# Pterodactyl_Application範例
key創建位置:/admin/api

## 基本設置
run.py

```py
from pteropy import Pterodactyl_Application
#導入套件

base_url = "https://面板網址"
api_key = "api key"
#key創建位置:/admin/api

#基本設定

ptero = Pterodactyl_Application(base_url, api_key)
#傳給套件
```

## 套件範例
run.py

```py
from pteropy import Pterodactyl_Application
base_url = "https://面板網址"
api_key = "api key"
ptero = Pterodactyl_Application(base_url, api_key)


ptero.check()  #檢查api連線狀態

ptero.create_user(username="用戶名",email="用戶email", password="密碼")  #創建用戶

ptero.list_users()  #所有用戶
```


# Pterodactyl_Client範例
key創建位置:/account/api

## 基本設置
run.py

```py
from pteropy import Pterodactyl_Client
#導入套件

base_url = "https://面板網址"
api_key = "api key"
#key創建位置:/account/api

#基本設定

ptero = Pterodactyl_Client(base_url, api_key)
#傳給套件
```

## 套件範例
run.py

```py
from pteropy import Pterodactyl_Client
base_url = "https://面板網址"
api_key = "api key"
ptero = Pterodactyl_Client(base_url, api_key)


ptero.check()  #檢查api連線狀態

ptero.account_details()  #帳戶資訊

ptero.details_2FA()  #生成TOTP 二維碼圖像以允許設置 2FA

ptero.enable_2FA()  #使用 details_2FA 請求生成的二維碼啟用 TOTP 2FA

ptero.disable_2FA()  #禁用帳戶上的 TOTP 2FA

ptero.update_email()  #更新帳戶的電子郵件位址

ptero.update_password()  #更新帳戶的密碼

ptero.list_API_keys()  #列出 API 金鑰

ptero.create_API_key()  #生成新的 API 金鑰

ptero.delete_API_key()  #刪除指定的 API 金鑰

ptero.get_server("3fa3d78d")  #獲得伺服器資料

ptero.list_servers()  #獲得伺服器列表

ptero.rename_server("3fa3d78d","名子")  #重命名伺服器

ptero.send_command("3fa3d78d","指令")  #發送指令

ptero.start_server("3fa3d78d")  #啟動伺服器

ptero.restart_server("3fa3d78d")  #重啟伺服器

ptero.stop_server("3fa3d78d")  #關閉伺服器

ptero.kill_server("3fa3d78d")  #強制關閉伺服器

#資料庫已經好了等待更新
```