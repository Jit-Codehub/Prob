import pandas as pd
from regex import F
import requests
from bs4 import BeautifulSoup
from .models import *; 
import os
# Create your views here.
def add_full_forms_to_database():
    for i in full_form_categories.objects.all():
        i.delete()
    for i in full_form_data.objects.all():
        i.delete()
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media')
    list_of_urls={'Full Forms':'full-form','Banking':'banking-full-forms',
                  'Educational':'educational-full-forms',
                  'Exam':'exam-full-forms','Gadgets':'gadgets-full-forms',
                  'Internet Slag':'internet-slang-full-forms',
                  'IT':'it-full-forms',
                  'Medical':'medical-full-forms',
                  'Organizational ':'organizational-full-forms',
                  'Telecom':'telecom-full-forms'}
    for ty in list_of_urls:
        cat=full_form_categories()
        cat.category=ty
        print(ty)
        cat.save()
        url="https://www.javatpoint.com/"+list_of_urls[ty]
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        full_form_tables=soup.find_all('table',class_="alt")
        for tbl in full_form_tables:
            full_form=tbl.find_all('a',class_="l1")
            for i in full_form:
                try:
                    full_form_categ=full_form_categories.objects.get(category=ty)
                    f=full_form_data()
                    url="https://www.javatpoint.com/"+i['href']
                    print(url)
                    count=full_form_data.objects.filter(full_form_abbr=i.get_text().lower()).count()
                    if count > 0:
                        f=full_form_data.objects.get(full_form_abbr=i.get_text().lower())
                        f.category=full_form_categ
                        f.save()
                    else:
                        f.full_form_abbr=i.get_text().lower()
                        r=requests.get(url)
                        soup=BeautifulSoup(r.content,'html.parser')
                        city=soup.find('div',{'id':'city'})
                        children=city.findChildren()
                        t=""
                        f.full_form=city.find('h2').get_text() 
                        for ch in children[6:len(children)-11]:
                            ch1=str(ch)
                            if str(ch).find('img')!=-1:
                                k=ch['src']
                                
                                if k.find("https://static.javatpoint.com/")==-1:
                                    # response=requests.get("https://static.javatpoint.com/"+k)
                                    image_name=k.split("/")[-1]
                                    print(image_name)
                                    # file=open(os.path.join(path,image_name),"wb")
                                    # file.write(response.content)
                                    # file.close()
                                    
                                    ch1=ch1.replace(k,"/media/"+image_name)
                                else:
                                    # response=requests.get(k)
                                    image_name=k.split("/")[-1]
                                    # file=open(os.path.join(path,image_name),"wb")
                                    # file.write(response.content)
                                    # file.close()
                                    ch1=ch1.replace(k,"/media/"+image_name)
                                ch=ch1
                            t+=str(ch)+""
                        f.content=t
                        f.category=full_form_categ
                        f.save()
                except:
                    pass
