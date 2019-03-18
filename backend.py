l=[]
def create_list():
    url="https://www.cricbuzz.com/cricket-match/live-scores"
    import requests
    from bs4 import BeautifulSoup
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    p=soup.findAll('div',attrs={'class':'cb-mtch-lst cb-col cb-col-100 cb-tms-itm'})
    
    for d in p:
        links=d.findAll('a')
        for a in links:
            l.append(a['href'])

def first_match():
    create_list()
    newurl="https://www.cricbuzz.com"+l[1]
    import requests
    from bs4 import BeautifulSoup
    r1=requests.get(newurl)
    soup1=BeautifulSoup(r1.text,'html.parser')
    p1=soup1.findAll('div',attrs={'class':'cb-col cb-col-67 cb-scrs-wrp'})
    l1=[]
    for p in p1:
        l1.append(p.get_text())
    return    (str(l1[0]))

def second_match():
    create_list()        
    newurl1="https://www.cricbuzz.com"+l[6]
    import requests
    from bs4 import BeautifulSoup
    r2=requests.get(newurl1)
    soup2=BeautifulSoup(r2.text,'html.parser')
    p2=soup2.findAll('div',attrs={'class':'cb-col cb-col-67 cb-scrs-wrp'})
    l2=[]
    for p in p2:
        l2.append(p.get_text())
    return ( str(l2[0]))
def live_matches():
    create_list()
    print("Current Matches Going Around...")
    newurl2="https://www.cricbuzz.com/cricket-match/live-scores"
    import requests
    from bs4 import BeautifulSoup
    r3=requests.get(newurl2)
    soup3=BeautifulSoup(r3.text,"html.parser")
    p3=soup3.findAll('h2',attrs={'class':'cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr'})
    l3=[]
    for x in p3:
        l3.append(x.get_text())
    return (l3)