# -*- coding: utf-8 -*-
import random
import requests
import re
from time import sleep
from bs4 import BeautifulSoup

files=["高德地图","百度地图","携程旅游","去哪儿"]
file=files[0]
User_Agent=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]
HEADERS = {
    'User-Agent':  User_Agent[random.randint(0,4)],  
    # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/201002201 Firefox/55.0',  
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',  
    'Accept-Encoding': 'gzip, deflate, br',  
    'Cookie': '',  
    'Connection': 'keep-alive',  
    'Pragma': 'no-cache',  
    'Cache-Control': 'no-cache'  
}

def getHTMLText(url):
    try:
        response= requests.get(url,headers=HEADERS,allow_redirects=False,timeout=5)  
        if response.status_code==200:
            html=response.content
            html=html.decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            return soup  
        else:  
            sleep(5)  
            print("等待ing")  
            return download_soup_waitting(url)
    except:
        return ''

def printAPPName(html):
    try:
        pattern = re.compile(r'{"im:name":{"label":(.*?)}, "rights"', re.S)
        #如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
        #而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配
        APPName = re.findall(pattern, str(html))
        return 'APPName:' + str(APPName)
    except:
        return ''

def fillUnivlist(titles, comments, stars, html):
    try:
        pattern = re.compile(r'"title":{"label":(.*?)}, "content"', re.S) #提取标题
        nbaInfo = re.findall(pattern, str(html)) #提取title

        # findStr = '"title":{"label":'
        # nbaInfo = nbaInfo1[nbaInfo1.find(findStr)+len(findStr):]
        patternFloor = re.compile(r'"content":{"label":(.*?), "attributes":{"type":"text"}}', re.S) #提取content
        floorText = re.findall(patternFloor, str(html))

        patternStar = re.compile(r'"im:rating":{"label":(.*?)}, "id"', re.S)  # 提取星级
        star = re.findall(patternStar, str(html))
        # print(str(star))

        number = len(nbaInfo)
        print(number)
        for i in range(number):
            Info = nbaInfo[i] #利用Tools类移除不想要的格式字符
            if i==0:Info = Info[Info.find('"title":{"label":')+len('"title":{"label":'):]
            # print(Info)
            Info1 = floorText[i]
            Info2 = star[i]
            # print(Info2+"hello")
            titles.append('title:' + Info)
            comments.append('content:' + Info1)
            stars.append('star:' + Info2)
    except:
        return ''

def writeText(titleText, fpath):
    try:
        with open(fpath, 'a', encoding='utf-8') as f:
            f.write(str(titleText)+'\n')
            f.write('\n')
            f.close()
    except:
        return ''

def writeUnivlist(titles, comments, stars, fpath, num):
    with open(fpath, 'a', encoding='utf-8') as f:
        for i in range(num):
            f.write(str(stars[i]) + '\n')
            f.write('*' * 10 + '\n')
            f.write(str(titles[i]) + '\n')
            f.write('*' * 50 + '\n') #输入一行*号
            f.write(str(comments[i]) + '\n')
            f.write('*' * 100 + '\n')
        f.close()

def main():
    count = 0
    url = 'https://itunes.apple.com/rss/customerreviews/page=1/id=461703208/sortby=mostrecent/json?l=en&&cc=cn' #要访问的网址
    output_file = "d://"+file+".txt" #最终文本输出的文件
    html = getHTMLText(url) #获取HTML
    APPName = printAPPName(html)
    writeText(APPName, output_file)
    for i in range(20):
        i = i + 1
        titles = []
        comments = []
        stars = []
        url = 'https://itunes.apple.com/rss/customerreviews/page=' + str(i) + '/id=461703208/sortby=mostrecent/json?l=en&&cc=cn'
        html = getHTMLText(url)
        #print(html)
        
        fillUnivlist(titles, comments, stars, html)
        writeUnivlist(titles, comments, stars, output_file, len(titles))
        
        count = count + 1
        print("\r当前进度: {:.2f}%".format(count * 100 / 10), end="")

if __name__ == '__main__':
    main()


