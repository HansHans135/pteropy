# pteropy
適用於Pterodactyl api的python庫

# 安裝
```pip install pteropy```

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

#創建用戶
ptero.create_user(username="用戶名",email="用戶email", password="密碼")
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

#獲得伺服器資料
ptero.get_server("3fa3d78d")

#啟動伺服器
ptero.start_server("3fa3d78d")
#重啟伺服器
ptero.restart_server("3fa3d78d")
#關閉伺服器
ptero.stop_server("3fa3d78d")
#強制關閉伺服器
ptero.kill_server("3fa3d78d")
```