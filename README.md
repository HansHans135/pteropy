# Pterodactyl.py
適用於Pterodactyl api的python庫

## 基本設置
run.py

```py
from ptpy import Pterodactyl_Application
#導入套件

base_url = "https://面板網址"
api_key = "api key"
#基本設定

ptero = Pterodactyl_Application(base_url, api_key)
#傳給套件
```