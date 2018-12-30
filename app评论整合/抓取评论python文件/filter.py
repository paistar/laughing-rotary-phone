# -*- coding: utf-8 -*-

files=["高德地图","百度地图","携程旅游","去哪儿"]
file=files[0]
count=0
infile=open("d://"+file+".txt",'r',encoding='utf-8')
#content = infile.read().decode('utf-8')
data=[]
for line in infile:
    #print(line)
    if line[0]=='c':
        #print(line)
        if "无意间" in line:
            continue
        if "无意中" in line:
            continue
        if "薇" in line:
            continue
        if "美女" in line:
            continue
        m=line[9:len(line)-2]
        #print(m)
        data.append(m)
        data.append('\n')
        count=count+1

infile.close()
print(data)

outfile=open("d://"+str(file)+"_new"+".txt",'w',encoding='utf-8')
for i in range(len(data)):
    outfile.write(data[i])
outfile.close()

