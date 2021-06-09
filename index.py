import requests
from dbtools import query
from filetools import write_file,read_file

# 获取首页轮播图
def test_01_lbt():
    url = "http://192.168.154.148/get_title_img"
    res = requests.get(url)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_02_regist():
    u1 = "http://192.168.154.148/regist"
    h1 = {"Content-Type":"application/json"}
    d1 = {"username":"chenwei2", "password":"123456abc","phone":"18212341234","email":"hhh@163.com"}
    res1 = requests.post(url=u1,heards=h1,json=d1)
    print(res1.text)