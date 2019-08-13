#%%
import requests
import json
import xlsxwriter

workbook = xlsxwriter.Workbook('tett.xlsx')
worksheet = workbook.add_worksheet("pchome")
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=SSD&page=1&sort=sale/dc"
print("YS")
res = requests.get(url)
data = json.loads(res.text)
webdata = data['prods']
webdata
len(webdata)
for row, product in enumerate(webdata):
    print(row)
    print(product['name'])
    print(product['price'])
    worksheet.write(row, 0, product['name'])
    worksheet.write(row, 1, product['price'])
workbook.close()
#%%
