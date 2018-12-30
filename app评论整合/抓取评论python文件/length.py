# -*- coding: utf-8 -*-
from matplotlib import pyplot

files=["高德地图","百度地图","携程旅游","去哪儿"]
file=files[0]
count=0
infile=open("d://"+str(file)+"_new"+".txt",'r',encoding='utf-8')
data=[]
length=[]
count=0
for line in infile:
    length.append(len(line))
    count=count+1


infile.close()
print(length)
print(count)

pyplot.hist(length,100)
pyplot.title('pdf')
pyplot.xlim(0.0,max(length)-100)
pyplot.show()