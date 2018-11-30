import mechanize
import bs4 as bs
import urllib
import os
import threading
import time
def banner():
    print("""


DDDDDDDDDDDDD       TTTTTTTTTTTTTTTTTTTTTTT   SSSSSSSSSSSSSSS
D::::::::::::DDD    T:::::::::::::::::::::T SS:::::::::::::::S
D:::::::::::::::DD  T:::::::::::::::::::::TS:::::SSSSSS::::::S
DDD:::::DDDDD:::::D T:::::TT:::::::TT:::::TS:::::S     SSSSSSS
  D:::::D    D:::::DTTTTTT  T:::::T  TTTTTTS:::::S
  D:::::D     D:::::D       T:::::T        S:::::S
  D:::::D     D:::::D       T:::::T         S::::SSSS
  D:::::D     D:::::D       T:::::T          SS::::::SSSSS
  D:::::D     D:::::D       T:::::T            SSS::::::::SS
  D:::::D     D:::::D       T:::::T               SSSSSS::::S
  D:::::D     D:::::D       T:::::T                    S:::::S
  D:::::D    D:::::D        T:::::T                    S:::::S
DDD:::::DDDDD:::::D       TT:::::::TT      SSSSSSS     S:::::S
D:::::::::::::::DD        T:::::::::T      S::::::SSSSSS:::::S
D::::::::::::DDD          T:::::::::T      S:::::::::::::::SS
DDDDDDDDDDDDD             TTTTTTTTTTT       SSSSSSSSSSSSSSS

Download                       TV               Series
""")
banner()
'''/////////////////////////browser work///////////////////////////////'''
sl=["http://sv4avadl.uploadt.com/","http://79.127.126.110/Serial/","http://dl8.heyserver.in/","http://dl2.funsaber.net/","http://dl6.downloadoo.ir","http://movie.downloadgozar.ir/"]
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
    menu()
    s=url[k]
    s1=s1+links[k]
    print(s1," selected ")
    lg(s1)
def dff(links):
    for link in links:
        try:
            os.system("wget %s"%link)
        except:
            pass
def menu(url):
    durl=[]
    for i in range(0,len(url)):
        f=str(i)+":"+s1+url[i]
        fs=s1+url[i]
        f = urllib.unquote(f).decode('utf8')
        durl.append(fs)
        print(f)

    number=input("enter your folder number:")
    if (number==1219):
        dff(durl)

    return number
print("select server ")
for i in range(0,len(sl)):
    a=str(i)+"."+sl[i]
    print(a)
dsa=input("choose a server :" )
s1=sl[dsa]
os.system("clear")
lg(sl[dsa])
