'''
1. get api sportsdb, daftar pemain suatu klub
2. input : klub apa? X
3. daftar pemain : nama, posisi, usia, negara
4. save X.xlsx, X.json, X.csv
'''

import requests
klub=input('Ketik klub : ')
url=f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data=requests.get(url)
players=data.json()['player']

import datetime as dt
x=dt.datetime.now()
tahun=int(x.strftime('%Y'))

header=['No','Nama','Posisi','Usia','Asal Negara']
pemain=[]
listPemain=[]
no=1
for player in players:
    usia=tahun-int(player['dateBorn'][:4])
    data=[]
    data.append(no)
    data.append(player['strPlayer'])
    data.append(player['strPosition'])
    data.append(usia)
    data.append(player['strNationality'])
    dictKlub=dict(zip(header,data))
    pemain.append(dictKlub)
    listPemain.append(data)
    no+=1

import json
with open(f'{klub}.json','w') as y:
    json.dump(pemain,y)

import csv
with open(f'{klub}.csv','w',newline='') as x:
    a=csv.DictWriter(x,fieldnames=header)
    a.writeheader()
    a.writerows(pemain)

import xlsxwriter
file=xlsxwriter.Workbook(f'{klub}.xlsx')
sheet=file.add_worksheet(f'{klub}')
for i in header:
    sheet.write(0,header.index(i),i)
row=1
for a,b,c,d,e in listPemain:
    sheet.write(row,0,a)
    sheet.write(row,1,b)
    sheet.write(row,2,c)
    sheet.write(row,3,d)
    sheet.write(row,4,e)
    row+=1
file.close()