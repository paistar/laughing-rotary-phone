# -*- coding: utf-8 -*-
from matplotlib import pyplot
files=["高德地图","百度地图","携程旅游","去哪儿"]
file=files[0]
count=0
infile=open("d://"+file+".txt",'r',encoding='utf-8')

star=[]
for line in infile:
    if line[0]=='s':
        star.append(line[6])

infile.close()
print(star)

count=[]
for i in range(5):
    count.append(int(0))

for item in star:
    count[int(item)-1]=count[int(item)-1]+1
    
print(count)