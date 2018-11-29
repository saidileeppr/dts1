import mechanize
import bs4 as bs
import os
import threading
import time
s1="http://sv4avadl.uploadt.com/"
def banner():
    print("dts")
banner()
'''/////////////////////////browser work///////////////////////////////'''
sl=["http://sv4avadl.uploadt.com"]
def lg(l1=sl[0]):
    global s1
    b=mechanize.Browser()
    b.set_handle_robots(False)   # ignore robots
    b.set_handle_refresh(False)  # can sometimes hang without this
    b.addheaders =[('User-agent', 'Firefox')]
    res=b.open(l1)
    bsf=bs.BeautifulSoup(res.read(),'lxml')
    links=[]
    files=[]
    url=[]
    for link in bsf.find_all('a', href=True):
        a=link['href']
        files.append(a)
        links.append(a)
    j=0
    for i in links:
        if(i.endswith('/')):
            u=sl[0]+'/'+i
            url.append(u)
            j=j+1
    k=menu(links)
    os.system("clear")
    s=url[k]
    s1=s1+links[k]
    print(s1," selected ")
    lg(s1)
def menu(url):
    for i in range(0,len(url)):
        f=str(i)+":"+url[i]
        print(f)
    number=input("enter your folder number:")
    return number
lg()
