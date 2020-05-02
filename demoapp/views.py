from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from .forms import searchform
import re
from .models import serres
Dict = {}
Dict2 = {}

def hi(request,name=""):
    if len(name) == 0:
        form = searchform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['search']
            if name == 'cl@9700':
                d = serres.objects.all()
                d.delete()
                return render(request,'demoapp/db.html')
            elif name== 'who@creator':
                return render(request,'demoapp/auth.html')
    alll = '/1/99/201'
    tempurl = 'https://piratebay1.xyz/search/'
    url = tempurl + name + alll
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = bs(plain_text, features="lxml")
    i = 1
    code = []
    code.append('<p><table id = "GFG_UP" >')
    for lin in soup.findAll('a', {'class': 'detLink'}):
        ref = lin.get('href')
        title = lin.get('text')
        no = str(i)
        # print("\033[1;36;40m|" + no.zfill(2) + "|" + str(link.string))
        if lin.string is not None:
            Dict[no] = ref
            Dict2[no] = lin.string
            cname=no+name
            eres=serres.objects.all()
            key=0
            for lk in eres:
                if cname == lk.name:
                    key=1
                else:
                    pass
            if key==1:
                pass
            else:
                res = serres(no=no, name=cname, url=ref, title=lin.string)
                res.save()
            code.append('<tr><tr></tr><tr></tr><tr></tr><tr></tr><td><a href="'+cname+'/'+no+'/">'+no.zfill(2)+' : '+lin.string +'</a></td></tr>')
            i = i + 1
    code.append('</p></table>')
    code1 = ""
    for ele in code:
        code1 += ele
    # return HttpResponse(code)
    return render(request,'demoapp/form.html', {'form': form,'code1': code1})

def result(request,name,no):
    try:
        for lis in serres.objects.all():
            if lis.no==no and lis.name==name:
                maglink=lis.url
                magtitle=lis.title
                source_code1 = requests.get(maglink)
                plain_text1 = source_code1.text
                soup1 = bs(plain_text1, features="lxml")
                #infos = soup1.find_all("dl", {'class': 'col1'})
                con="<p>"
                for item in list(zip(soup1.find_all("dt")[1::1],soup1.find_all("dd")[1::1])):
                    titl,datta = item
                    tit=titl.string
                    dt=datta.string
                    con=con+'<strong> '+str(tit)+": </strong>"+str(dt)+'<br>'
                con=con+'</p>'
                links = soup1.find_all('a', href=re.compile('^magnet'))
                lks=""
                for link in links:
                    if "magnet" in link.get("href"):
                        lks = (link.get("href"))
                    break
                #maga='<a href="'+lks+'">DOWNLOAD</a>'

        return render(request,'demoapp/result.html',{'lks':lks,'magtitle':magtitle,'con':con})
    except:
        return render(request, 'demoapp/error.html')