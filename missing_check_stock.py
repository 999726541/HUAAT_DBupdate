#-*- coding:UTF-8 -*-
import csv
def stockjj_daily_check(date):
    f = open('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\过往场内基金净值.csv','r',encoding = 'utf-8')#读取中文标题，可以用rb来读取，但是byte不能被代送
    reader =csv.reader(f)
    codedownload = []
    for c1,c2,c3,c4,c5,c6,c7,c8 in reader:#只能用r模式来代送
        if c1 not in codedownload:
            codedownload.append(c1)
    count=0
    f = open('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\过往场内基金净值extra.csv','r',encoding = 'utf-8')#读取中文标题，可以用rb来读取，但是byte不能被代送
    reader =csv.reader(f)
    for c1,c2,c3,c4,c5,c6,c7,c8 in reader:#只能用r模式来代送
        if c1 not in codedownload:
            codedownload.append(c1)

    print(len(codedownload))
    f2 = open('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\场内基金每日净值.csv','r',encoding='utf-8')
    f2.readline()
    codemis = open('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\过往基金净值missing.txt','w')#吧meaning bytes-like object required,不是byte就不用b
    reader = csv.reader(f2)
    codemissed=[]
    for c1,c2,c3,c4 in reader:
        if c1 not in codedownload:
            codemis.write(str(c1)+'\n')
            codemissed.append(c1)
        if c2 == date:
            count+=1
    codemis.close()
    print('missing：'+str(len(codemissed)))
    print('today updated: '+str(count))
