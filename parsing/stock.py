#%%
# step1. import package
import requests
import json
import pandas as pd
from io import StringIO

def stock_info(datatime, stock_num):
    stock_url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datatime + '&type=ALL'
    stock_req = requests.post(stock_url)
    stock_list = []
    for idx in stock_req.text.split('\n'):
        if len(idx.split('",')) == 17 and idx[0] != '=' :
            idx = idx.strip(",\r\n")
            stock_list.append(idx)

    stock_df = pd.read_csv(StringIO("\n".join(stock_list)))
    pd.set_option('display.max_rows', None)
    if stock_num.isdigit():
        stock_index = list(stock_df['證券代號']).index(stock_num)
    else:
        stock_index = list(stock_df['證券名稱']).index(stock_num)
    return stock_df.loc[stock_index:stock_index].to_html(index=False)

def stock_dividend(stock_num):
    stock_url = "https://mops.twse.com.tw/mops/web/ajax_t05st09_1"
    form_data = {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'co_id':int(stock_num),
        'TYPEK':"all",
        'isnew':"false"
    }

    r = requests.post(stock_url, form_data)
    html_df = pd.read_html(r.text)[1].fillna("")
    return html_df.to_html(index=False)


'''
with open('stock_info.html', 'w') as sotck_file:
    sotck_file.write(stock_dividend('2454'))

with open('stock_info.html', 'a') as sotck_file:
    sotck_file.write(stock_info('20191119', '2454'))
'''

stock_url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20191120&stockNo=2454&_=1574264462881'
stock_req = requests.get(stock_url)
data = json.loads(stock_req.text)
print(data['title'])
print(data['fields'])
for row in data['data']:
    print(row)
# %%
