from django import template
import re
register = template.Library()

from bs4 import BeautifulSoup as bs
def split(value):
        try:
            return value.split(":")[1]
        except:
            return value

register.filter('split', split)

def replace_img(value):
    soup=bs(value,'html.parser')
    images=soup.find_all('img')
    for i in images:
        k=i['src']
        i['src']="https://static.javatpoint.com/"+k
        if k.find("https://static.javatpoint.com/")==-1:
            value=value.replace(k,i['src'])
        print(i['src'])
    return value
    

register.filter('replace_img', replace_img)
def replace(value):
    value=value.strip()
    return value.replace(" ","-")

register.filter('replace', replace)

def replace1(value):
    value=value.strip()
    return value.replace("-"," ")

register.filter('replace1', replace1)

def replace_slash(value):
    value=value.strip()
    return value.replace("/",",")

register.filter('replace_slash', replace_slash)

def times(number,current_page):
    if number <= 5:
        return range(number)
    else:
        if current_page>=5:
            return range(current_page-5,current_page)
        else:
            return range(0,5)

register.filter('times', times)

def modulus(num1,num2):
    return int(num1)//int(num2)

register.filter('modulus', modulus)