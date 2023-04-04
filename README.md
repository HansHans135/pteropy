# pteropy
適用於Pterodactyl api的python庫

# 安裝
```pip install pteropy```
## 基本設置
run.py

```py
from pteropy import Pterodactyl_Application
#導入套件

base_url = "https://面板網址"
api_key = "api key"
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