# PChome 爬蟲程式
##程式主畫面
![iamge](https://github.com/lsc25846/PChome-crawler/blob/main/%E5%9C%96%E7%89%87/GPU_%E4%B8%BB%E7%95%AB%E9%9D%A2.png)

##功能
此程式可以自動爬出PChome上的商品資訊，包含商品的ID、名稱以及價格。透過MariaDB來進行資料存儲以及管理。

##安裝流程
### 1.請先安裝requirements
'''
pip install -r requirements.txt
'''

### 2.匯入gpu.sql
先匯入gpu.sql
![image]()
再按F9或是執行按鈕
![image]()

### 3.請在主程式(fetchGPU.py)中修改資料庫的使用者以及密碼

'''python
db_manager = DatabaseManager(host="localhost", user="root", password="user", database="leadtek", logger=logger)
'''

##使用方式
在搜尋欄裡輸入要找查的商品名稱後按下搜尋即可。
![image](https://github.com/lsc25846/PChome-crawler/blob/main/%E5%9C%96%E7%89%87/%E6%90%9C%E5%B0%8B%E7%95%AB%E9%9D%A2.png)
