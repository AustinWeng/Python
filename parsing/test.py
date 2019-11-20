#引入包
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("http://fund.eastmoney.com/fund.html")
html = response.read();

#這個網頁編碼是gb2312
#print(html.decode("gb2312"))

#把html內容儲存到一個檔案
with open("1.txt","wb") as f:
    f.write(html.decode("gb2312").encode("utf8"))
    f.close()


with open("1.txt", "rb") as f:
    html = f.read().decode("utf8")
    f.close()

# 分析html內容
soup = BeautifulSoup(html,"html.parser")

# 取出網頁title
print(soup.title) #<title>每日開放式基金淨值表 _ 天天基金網</title>

# 基金編碼
codes = soup.find("table",id="oTable").tbody.find_all("td","bzdm")

result = () # 初始化一個元組
for code in codes:
    result += ({
        "code":code.get_text(),
        "name":code.next_sibling.find("a").get_text(),
        "NAV":code.next_sibling.next_sibling.get_text(),
        "ACCNAV":code.next_sibling.next_sibling.next_sibling.get_text()
     },)
for item in result:
    print(item["name"]+"---"+item["NAV"])
# 列印結果
print(result[0]["name"])