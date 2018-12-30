# -*- coding: utf-8 -*-

files=["高德地图","百度地图","携程旅游","去哪儿"]
file=files[3]
count=0
infile=open("d://"+file+".txt",'r',encoding='utf-8')
data=[[],[],[],[],[]]
flag=0

for line in infile:
    #print(line)
    if line[0]=='s':
        flag=int(line[6])
        continue

    if line[0]=='c':
        if "无意间" in line:
            continue
        if "无意中" in line:
            continue
        if "薇" in line:
            continue
        if "美女" in line:
            continue
        m=line[9:len(line)-2]
        data[flag-1].append(m)
        data[flag-1].append('\n')


infile.close()
print(data)

for i in range(5):
    outfile=open("d://"+str(file)+"_"+str(i+1)+".txt",'w',encoding='utf-8')
    for j in range(len(data[i])):
        outfile.write(data[i][j])
    outfile.close()
