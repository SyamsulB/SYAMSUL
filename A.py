import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[0;36m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def clear():
	os.system('clear')
def back():
	login()
# BANNER
def banner():
	print('''%s"""%(N))                                                    
\n'''%(N,N,N,N))
def kontol():
    os.system("clear")
    print(f""" """)
def licensi():#line:42
  try :#line:43
    os .system ('clear')
    kontol()
    print (f"""
""")#line:49
    OOO00O0OOO00OO00O =input (f"\x1b[1;97m╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n\x1b[1;97m│\x1b[1;93m   _________                                  .__   \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m  /   _____/__.__._____    _____   ________ __|  |  \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m  \_____  <   |  |\__  \  /     \ /  ___/  |  \  |  \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m  /        \___  | / __ \|  Y Y  \\___ \|  |  /  |__ \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m /_______  / ____|(____  /__|_|  /____  >____/|____/\x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m         \/\/          \/      \/     \/   \x1b[1;90mV \x1b[1;97m: \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10 \x1b[1;97m│\n\x1b[1;97m╰────────────────────────────────────────────────────╯\n          ─━㋱[\033[41m\033[1;37m Author : Syamsul Bahri \x1b[0m]㋱━─         \n\x1b[1;97m╭────────────────────────────────────────────────────╮\n\x1b[1;97m│\x1b[1;93m [\x1b[1;97m1\x1b[1;93m] \x1b[1;97mCRACK FILE CLONING  \x1b[1;93m [\x1b[1;97m6\x1b[1;93m] \x1b[1;97mLOGIN \033[1;32mCOOKIE V1       \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m [\x1b[1;97m2\x1b[1;93m] \x1b[1;97mLOGIN \033[1;32mTOKEN \x1b[1;97m& \033[1;32mCOOKIE \x1b[1;93m[\x1b[1;97m7\x1b[1;93m]\x1b[1;97m CRACK EMAIL FACEBOOK  \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m [\x1b[1;97m3\x1b[1;93m] \x1b[1;97mLOGIN AKUN FB       \x1b[1;93m [\x1b[1;97m8\x1b[1;93m] \x1b[1;97mCRACK FB ID 2010-12   \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m [\x1b[1;97m4\x1b[1;93m] \x1b[1;97mCRACK FB ID 2008-09  \x1b[1;93m[\x1b[1;97m9\x1b[1;93m] \x1b[1;97mCRACK FB ID 2004-05   \x1b[1;97m│\n\x1b[1;97m│\x1b[1;93m [\x1b[1;97m5\x1b[1;93m] \x1b[1;97mCRACK FB ID 2011-14 \x1b[1;93m [\x1b[1;97m0\x1b[1;93m] \x1b[1;97mCRACK FB ID 2006-07   \x1b[1;97m│\n\x1b[1;97m╰──\x1b[1;90m╭\x1b[1;97m[\x1b[1;92mMENU\x1b[1;97m]───────────────────────────────────────────╯\n \x1b[1;90m  └──\x1b[1;93m✪\x1b[1;97m➣ \x1b[1;92m ")#line:50
    if OOO00O0OOO00OO00O in ['1','01']:#line:51
      print (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m Anda Akan Diarahkan Ke Whatsapp...");time .sleep (3 );os .system ('xdg-open https://wa.me/6282261310817?text=Premium+Bocil²+Bangsat+No+Free.......???????');exit ()#line:52
    elif OOO00O0OOO00OO00O in ['2','02']:#line:53
      O000O000OOO000OOO =input (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m MASUKAN\033[1;32m TOKEN \x1b[1;97m& \033[1;32mCOOKIE :{K} ")#line:54
      if len (O000O000OOO000OOO )==0 :#line:55
        exit (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m Updated Dulu")#line:56
      else :#line:57
        with requests .Session ()as O0O0OO0O0O00OOOO0 :#line:58   #### ISI TOKEN LU DAN   ID LU
          OOO00OO00O0O0OOOO =O0O0OO0O0O00OOOO0 .get(f'https://app.cryptolens.io/api/key/activate?token=WyIxNjk4MzkyOCIsIktFWUhHaUJzQkZzcEpTdXFRMXh0ZUh3U0crOWpyNk9LM1ZWV0xSQlkiXQ==&ProductId=14877&Key={O000O000OOO000OOO}&Sign=True').json ()['licenseKey']#line:59
          open ('apikey.txt','w').write (O000O000OOO000OOO )#line:60
          print (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m Expired :{K} {OOO00OO00O0O0OOOO['expires'].split('T')[0]}");time .sleep (2 );login()#line:61
    elif OOO00O0OOO00OO00O in ['3','03']:#line:62
      exit ()#line:63
    else :#line:64
      exit (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m Daftar Premium Dulu")#line:65
  except (KeyError ):#line:66
    exit (f" \x1b[1;93m [\x1b[1;97m•\x1b[1;93m]\x1b[1;97m Anda Bukan Anggota Premium")#line:67
  except Exception as O0OO00OOO000OOO00 :#line:68
    exit (f"{P}[{M}!{P}]{M} {O0OO00OOO000OOO00}")#line:69

balmond = O+"["+J+"•"+O+"]"
		
if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	licensi()
