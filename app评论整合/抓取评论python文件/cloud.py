# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt


file="去哪儿"
'''
count=0
infile=open("d://"+file+".txt",'r',encoding='utf-8')
#content = infile.read().decode('utf-8')
data=[]
for line in infile:
    #print(line)
    if line[0]=='c':
        #print(line)
        if "无意中" in line:
            continue
        if "ASO排名优化" in line:
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
'''
text=open("d://"+file+"_new.txt",encoding='utf-8').read()
font = "C:\Windows\Fonts\msyh.ttc"
wordcloud = WordCloud(background_color='white',width=5000, height=3000, margin=2,font_path=font).generate(text)
plt.figure(figsize=(16,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()