from django.http import request
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import math
from .unitConverter import power_raise
from scipy.stats import binom,norm,t,lognorm
from functools import reduce
import operator as op
import random
from itertools import combinations
from portal.models import *
from django.template.context import RequestContext
# from . import triangle_law_of_cosines_calculations as tlc
#COIN TOSS PROBABILITY VIEW
def home(request):
        portal_obj = HomepageBlog.objects.filter(app="probability",status="Published")
        context = {"portal_obj":portal_obj.first() if portal_obj else None}
        return render(request,'base/Probability_calculator.html',context)
def privacy_policy(request):
         return render(request,'base/privacy_policy.html')
def disclaimer(request):
         return render(request,'base/disclaimer.html')
def accuracy_calculator(request):
    try:
        Given = request.POST.get('Given','form1')
        tp = request.POST.get('tp')
        tn = request.POST.get('tn')
        fp = request.POST.get('fp')
        fn = request.POST.get('fn')
        p = request.POST.get('p')
        ov = request.POST.get('ov')
        av = request.POST.get('av')
    

        if request.method == "POST":
            if Given == 'form1' and tp and tn and fn and fp and request.method == "POST":
                Given = request.POST.get('Given')
                tp = float(request.POST.get('tp'))
                tn = float(request.POST.get('tn'))
                fp = float(request.POST.get('fp'))
                fn = float(request.POST.get('fn'))

                re = ((tp + tn) / (tp + tn + fp + fn))*100

                context = {
                'tp':tp,
                'Given':Given,
                'tn':tn,
                'fp':fp,
                'fn':fn,
                'result':round(re,4),
                'ot':True,
                "tp":tp,
                "tn":tn,
                "fp":fp,
                "fn":fn
                }
                return render(request, 'PROBABILITY/accuracy-calculator.html',context)

            elif Given == 'form2' and p and tp and tn and fn and fp and request.method == "POST":
                Given = request.POST.get('Given')
                p = float(request.POST.get('p'))
                tp = float(request.POST.get('tp'))
                tn = float(request.POST.get('tn'))
                fp = float(request.POST.get('fp'))
                fn = float(request.POST.get('fn'))

                sp = (tn / (fp + tn))
                se = (tp / (tp + fn))

                re = (((se)* (p/100)) + ((sp)* (1 - (p/100))))*100


                context = {
                'tp':tp,
                'Given':Given,
                'tn':tn,
                'fp':fp,
                'fn':fn,
                'sp':round(sp,4),
                'se':round(se,4),
                'p':p,
                'result':round(re,4),
                'ot':True,
                "tp":tp,
                "tn":tn,
                "fp":fp,
                "fn":fn
                }
                return render(request, 'PROBABILITY/accuracy-calculator.html',context)

            elif Given == 'form3' and av and ov and request.method == "POST":
                Given = request.POST.get('Given')
                ov = float(request.POST.get('ov'))
                av = float(request.POST.get('av'))

                re = (abs(ov - av) / av) * 100

                context = {
                'ov':ov,
                'av':av,
                'Given':Given,
                'result':round(re,4),
                'ot':True,
                "tp":tp,
                "tn":tn,
                "fp":fp,
                "fn":fn
                }
                return render(request, 'PROBABILITY/accuracy-calculator.html',context)
            return render(request, 'PROBABILITY/accuracy-calculator.html',{'ov':50,'av':25,'tp':30,'tn':50,'fp':40,'fn':60,'p':40,'ot':False,'Given':Given})
        return render(request, 'PROBABILITY/accuracy-calculator.html',{'ov':50,'av':25,'tp':30,'tn':50,'fp':40,'fn':60,'p':40,'ot':False,'Given':Given})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request, 'PROBABILITY/accuracy-calculator.html',{'ov':50,'av':25,'tp':30,'tn':50,'fp':40,'fn':60,'p':40,'ot':False,'Given':Given})


def bayes_theorem_calculator(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        description={}
        description['l1_bold']="Bayes Theorem : P(A/B) = (P(B/A)*P(B)) / P(A)"
        if(float(a)>100 or float(b)>100 or float(c)>100 or float(a)<1 or float(b)<1 or float(c)<1):
            messages.info(request,"Invalid Value")
            return render(request, 'PROBABILITY/baye_s-theorem-calculator.html')
        else:
            description['l2']="P(B/A) = ( "+c+" * "+b+" ) / "+a
            d=float(c)*float(b)/float(a)
            description['l3']="P(B/A) = "+str(d)
            return render(request, 'PROBABILITY/baye_s-theorem-calculator.html',context={'a':a,'b':b,"c":c,"d":d,"answer":description})
    return render(request, 'PROBABILITY/baye_s-theorem-calculator.html',context={'a':5,'b':5,"c":5})



def binomial_probability_distribution_calculator(request):
    try:
        r = request.POST.get('r')
        p = request.POST.get('p')
        n = request.POST.get('n')
        
        ot = False
        if request.method == "POST":
            r = float(request.POST.get('r'))
            p = float(request.POST.get('p'))
            n = float(request.POST.get('n'))
            def facto(n):
                f=1
                for i in range(1,int(n+1)):
                    f=f*i
                return f
            
            nf = facto(n)
            rf = facto(r)
            nrf = facto(n-r)
            ncr = nf/ (rf * nrf)
            pr = p**r
            p1 = 1-p 
            nr = n-r
            re =  ncr * pr * (p1**nr)


            context = {
            'p':p,
            'r':r,
            'n':n,
            'nf':nf,
            'rf':rf,
            'nrf':nrf,
            'pr':pr,
            'p1':p1,
            'nr':nr,
            'ncr':ncr,
            'result':round(re,5),
            'ot':True               
             }

            return render(request,'PROBABILITY/binomial-probability-distribution-calculator.html',context)
        else:
            return render(request,'PROBABILITY/binomial-probability-distribution-calculator.html',{'r':7,'n':12,'p':0.5,'ot':False})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'PROBABILITY/binomial-probability-distribution-calculator.html',{'r':7,'n':12,'p':0.5,'ot':False})



def chi_square_probability_calculator(request):
    try:
        ov = request.POST.get('ov')
        ev = request.POST.get('ev')
        
        
        ot = False
        if request.method == "POST":
            ov = float(request.POST.get('ov'))
            ev = float(request.POST.get('ev'))
            
            re = ((ov - ev)**2) / ev            

            context = {
            'ov':ov,
            'ev':ev,
            'result':round(re,5),
            'ot':True               
             }

            return render(request,'PROBABILITY/chi-square-probability-calculator.html',context)
        else:
            return render(request,'PROBABILITY/chi-square-probability-calculator.html',{'ov':5,'ev':9,'ot':False})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'PROBABILITY/chi-square-probability-calculator.html',{'ov':5,'ev':9,'ot':False})



def birthday_paradox_calculator(request):
    if request.method=="POST":
        a=request.POST['a']
        if(int(a)<1):
            messages.info(request,"Invalid Value")
        else:
            d=int(a)*(int(a)-1)/2
            ans=(1-((364/365)**d))*100
            return render(request, 'PROBABILITY/birthday-paradox-calculator.html',context={'a':a,"d":ans})
    return render(request, 'PROBABILITY/birthday-paradox-calculator.html',context={'a':5})
def Roundoff(n):
  base=""
  power=""
  n='%.2E' % n
  s=str(n)
  base=""
  power=""
  f=False
  for i in range(0,len(s)):
    if s[i]=='E':
        f=True
        continue
    if f:
        power+=s[i]
    else:
        base+=s[i]           
   
  return base,power
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

def binomial_probability_calculator(request):
    if request.method == 'POST':
        given_data = request.POST.get('given_data')

        if request.POST.get('tr')!=None and request.POST.get('tr')!='':
            inp=str(request.POST.get('tr'))
            if inp.isdigit():
                tr=int(request.POST.get('tr'))
            else:
                tr=float(request.POST.get('tr'))
        else:
            tr=None

        if request.POST.get('pr')!=None and request.POST.get('pr')!='':
            inp=str(request.POST.get('pr'))
            if inp.isdigit():
                pr=int(request.POST.get('pr'))
            else:
                pr=float(request.POST.get('pr'))
        else:
            pr=None

        if request.POST.get('sc')!=None and request.POST.get('sc')!='':
            inp=str(request.POST.get('sc'))
            if inp.isdigit():
                sc=int(request.POST.get('sc'))
            else:
                sc=float(request.POST.get('sc'))
        else:
            sc=None

        
        
        if given_data=="form1" and tr and pr and sc:

            #copy the values:
            tr1 = tr
            pr1 = pr
            sc1 = sc            

            #calculations
            ftr = math.factorial(tr)
            fsc = math.factorial(sc)
            fts = math.factorial(tr-sc)
            frst = (ftr/(fsc*fts))
            frst1 = (pr**sc)
            frst2 = ((1-pr)**(tr-sc))
           

            
            ans = frst*frst1*frst2
            

            ans2={}
            for x in range(0, tr+1):
                ans2[str(x)] = round(ftr/(math.factorial(x)*(math.factorial(abs(tr-x))))*(pr**x)*((1-pr)**(abs(x-tr))),4)
            #print(ans2)
      

            #round Off
            if not ( (tr>=1 and tr<=10000) or (round(tr,3)!=0 and round(tr,3)!=0.001)):
                base1,power1=Roundoff(tr)
                tr=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                tr=round(tr,3)
       
            if not  ((pr>=1 and pr<=10000) or (round(pr,3)!=0 and round(pr,3)!=0.001)):
                base1,power1=Roundoff(pr)
                pr=f"{base1} X 10"+add_tags('sup',power1)
            else:
                pr=round(pr,3) 

            if not  ((sc>=1 and sc<=10000) or (round(sc,3)!=0 and round(sc,3)!=0.001)):
                base1,power1=Roundoff(sc)
                sc=f"{base1} X 10"+add_tags('sup',power1)
            else:
                sc=round(sc,3) 
            
            if not ( (fts>=1 and fts<=10000) or (round(fts,3)!=0 and round(fts,3)!=0.001)):
                base1,power1=Roundoff(fts)
                fts=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                fts=round(fts,3)
       
            if not  ((frst>=1 and frst<=10000) or (round(frst,3)!=0 and round(frst,3)!=0.001)):
                base1,power1=Roundoff(frst)
                frst=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst=round(frst,3) 
    
            if not  ((ans>=1 and ans<=10000) or (round(ans,3)!=0 and round(ans,3)!=0.001)):
                base1,power1=Roundoff(ans)
                ans=f"{base1} X 10"+add_tags('sup',power1)
            else:
                ans=round(ans,4)  

            if not  ((frst1>=1 and frst1<=10000) or (round(frst1,3)!=0 and round(frst1,3)!=0.001)):
                base1,power1=Roundoff(frst1)
                frst1=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst1=round(frst1,3) 

            if not  ((frst2>=1 and frst2<=10000) or (round(frst2,3)!=0 and round(frst2,3)!=0.001)):
                base1,power1=Roundoff(frst2)
                frst2=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst2=round(frst2,3) 
           

             

            context={
                'ftr':ftr,
                'frst':frst,
                'frst1':frst1,
                'frst2':frst2,
                'fsc':fsc,
                'fts':fts,
                'tr':tr,
                'pr':pr,
                'sc':sc,
                'tr1':tr1,
                'pr1':pr1,
                'sc1':sc1,
                'x':x,
                'ans2':ans2,
                
              
                
                'ans':ans,
                
                'given_data':given_data,
                }
            return render(request,'PROBABILITY/binomial-probability-calculator.html',context)
    

        if given_data=="form2" and tr and pr and sc:

            #copy the values:
            tr1 = tr
            pr1 = pr
            sc1 = sc            

            #calculations
            ftr = math.factorial(tr)
            fsc = math.factorial(sc)
            fts = math.factorial(tr-sc)
            frst = (ftr/(fsc*fts))
            frst1 = (pr**sc)
            frst2 = ((1-pr)**(tr-sc))
           


            
            ans = frst*frst1*frst2

            an = {}
           
            for y in range(0,sc):
                an[str(y)] = round(ftr/(math.factorial(y)*(math.factorial(abs(tr-y))))*(pr**y)*((1-pr)**(abs(y-tr))),4)
            values = an.values()
            total = sum(values)
               
            
            ans2={}
            for x in range(0, tr+1):
                ans2[str(x)] = round(ftr/(math.factorial(x)*(math.factorial(abs(tr-x))))*(pr**x)*((1-pr)**(abs(x-tr))),4)
            #print(ans2)

            #round Off
            if not ( (tr>=1 and tr<=10000) or (round(tr,3)!=0 and round(tr,3)!=0.001)):
                base1,power1=Roundoff(tr)
                tr=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                tr=round(tr,3)
       
            if not  ((pr>=1 and pr<=10000) or (round(pr,3)!=0 and round(pr,3)!=0.001)):
                base1,power1=Roundoff(pr)
                pr=f"{base1} X 10"+add_tags('sup',power1)
            else:
                pr=round(pr,3) 

            if not  ((sc>=1 and sc<=10000) or (round(sc,3)!=0 and round(sc,3)!=0.001)):
                base1,power1=Roundoff(sc)
                sc=f"{base1} X 10"+add_tags('sup',power1)
            else:
                sc=round(sc,3) 
            
            if not ( (fts>=1 and fts<=10000) or (round(fts,3)!=0 and round(fts,3)!=0.001)):
                base1,power1=Roundoff(fts)
                fts=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                fts=round(fts,3)
       
            if not  ((frst>=1 and frst<=10000) or (round(frst,3)!=0 and round(frst,3)!=0.001)):
                base1,power1=Roundoff(frst)
                frst=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst=round(frst,3) 
            
            if not  ((total>=1 and total<=10000) or (round(total,4)!=0 and round(total,4)!=0.001)):
                base1,power1=Roundoff(total)
                total=f"{base1} X 10"+add_tags('sup',power1)
            else:
                total=round(total,4) 
    
            if not  ((ans>=1 and ans<=10000) or (round(ans,4)!=0 and round(ans,4)!=0.001)):
                base1,power1=Roundoff(ans)
                ans=f"{base1} X 10"+add_tags('sup',power1)
            else:
                ans=round(ans,4)

             

            if not  ((frst1>=1 and frst1<=10000) or (round(frst1,3)!=0 and round(frst1,3)!=0.001)):
                base1,power1=Roundoff(frst1)
                frst1=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst1=round(frst1,3) 

            if not  ((frst2>=1 and frst2<=10000) or (round(frst2,3)!=0 and round(frst2,3)!=0.001)):
                base1,power1=Roundoff(frst2)
                frst2=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst2=round(frst2,3) 
           

             

            context={
                'values':values,
                'total':total,
                'ftr':ftr,
                'frst':frst,
                'frst1':frst1,
                'frst2':frst2,
                'fsc':fsc,
                'fts':fts,
                'tr':tr,
                'pr':pr,
                'sc':sc,
                'tr1':tr1,
                'pr1':pr1,
                'sc1':sc1,
                'x':x,
                'ans2':ans2,
                'y':y,
                'an':an,
            
                
              
                
                'ans':ans,
                
                'given_data':given_data,
                }

                 
       
            return render(request,'PROBABILITY/binomial-probability-calculator.html',context)

        if given_data=="form3" and tr and pr and sc:

            #copy the values:
            tr1 = tr
            pr1 = pr
            sc1 = sc            

            #calculations
            ftr = math.factorial(tr)
            fsc = math.factorial(sc)
            fts = math.factorial(tr-sc)
            frst = (ftr/(fsc*fts))
            frst1 = (pr**sc)
            frst2 = ((1-pr)**(tr-sc))
            

            
            ans = frst*frst1*frst2
            an = {}
           
            for y in range(0,sc+1):
                an[str(y)] = round(ftr/(math.factorial(y)*(math.factorial(abs(tr-y))))*(pr**y)*((1-pr)**(abs(y-tr))),4)
            values = an.values()
            total = sum(values)
               
            
            ans2={}
            for x in range(0, tr+1):
                ans2[str(x)] = round(ftr/(math.factorial(x)*(math.factorial(abs(tr-x))))*(pr**x)*((1-pr)**(abs(x-tr))),4)
            #print(ans2)

            #round Off
            if not ( (tr>=1 and tr<=10000) or (round(tr,3)!=0 and round(tr,3)!=0.001)):
                base1,power1=Roundoff(tr)
                tr=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                tr=round(tr,3)
       
            if not  ((pr>=1 and pr<=10000) or (round(pr,3)!=0 and round(pr,3)!=0.001)):
                base1,power1=Roundoff(pr)
                pr=f"{base1} X 10"+add_tags('sup',power1)
            else:
                pr=round(pr,3) 

            if not  ((sc>=1 and sc<=10000) or (round(sc,3)!=0 and round(sc,3)!=0.001)):
                base1,power1=Roundoff(sc)
                sc=f"{base1} X 10"+add_tags('sup',power1)
            else:
                sc=round(sc,3) 
            
            if not ( (fts>=1 and fts<=10000) or (round(fts,3)!=0 and round(fts,3)!=0.001)):
                base1,power1=Roundoff(fts)
                fts=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                fts=round(fts,3)
       
            if not  ((frst>=1 and frst<=10000) or (round(frst,3)!=0 and round(frst,3)!=0.001)):
                base1,power1=Roundoff(frst)
                frst=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst=round(frst,3)

            if not  ((total>=1 and total<=10000) or (round(total,4)!=0 and round(total,4)!=0.001)):
                base1,power1=Roundoff(total)
                total=f"{base1} X 10"+add_tags('sup',power1)
            else:
                total=round(total,4)  
    
            if not  ((ans>=1 and ans<=10000) or (round(ans,4)!=0 and round(ans,4)!=0.001)):
                base1,power1=Roundoff(ans)
                ans=f"{base1} X 10"+add_tags('sup',power1)
            else:
                ans=round(ans,4) 

            if not  ((frst1>=1 and frst1<=10000) or (round(frst1,3)!=0 and round(frst1,3)!=0.001)):
                base1,power1=Roundoff(frst1)
                frst1=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst1=round(frst1,3) 

            if not  ((frst2>=1 and frst2<=10000) or (round(frst2,3)!=0 and round(frst2,3)!=0.001)):
                base1,power1=Roundoff(frst2)
                frst2=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst2=round(frst2,3) 
           

             

            context={
                'ftr':ftr,
                'frst':frst,
                'frst1':frst1,
                'frst2':frst2,
                'fsc':fsc,
                'fts':fts,
                'tr':tr,
                'pr':pr,
                'sc':sc,
                'tr1':tr1,
                'pr1':pr1,
                'sc1':sc1,
                'x':x,
                'y':y,
                'an':an,
                'ans2':ans2,
                'total':total,
                'values':values,
                
              
                
                'ans':ans,
                
                'given_data':given_data,
                }

                 
       
            return render(request,'PROBABILITY/binomial-probability-calculator.html',context)

        if given_data=="form4" and tr and pr and sc:

            #copy the values:
            tr1 = tr
            pr1 = pr
            sc1 = sc            

            #calculations
            cc = sc+1
            ftr = math.factorial(tr)
            fsc = math.factorial(cc)
            fts = math.factorial(tr-cc)
            frst = (ftr/(fsc*fts))
            frst1 = (pr**cc)
            frst2 = ((1-pr)**(tr-cc))
            


            
            ans = frst*frst1*frst2
            an = {}
            for y in range(sc+1 , tr+1 ):
                an[str(y)] = round(ftr/(math.factorial(y)*(math.factorial(abs(tr-y))))*(pr**y)*((1-pr)**(abs(y-tr))),4)
            values = an.values()
            total = sum(values)
               
            
            ans2={}
            for x in range(0, tr+1):
                ans2[str(x)] = round(ftr/(math.factorial(x)*(math.factorial(abs(tr-x))))*(pr**x)*((1-pr)**(abs(x-tr))),4)
            #print(ans2)

            #round Off
            if not ( (tr>=1 and tr<=10000) or (round(tr,3)!=0 and round(tr,3)!=0.001)):
                base1,power1=Roundoff(tr)
                tr=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                tr=round(tr,3)
       
            if not  ((pr>=1 and pr<=10000) or (round(pr,3)!=0 and round(pr,3)!=0.001)):
                base1,power1=Roundoff(pr)
                pr=f"{base1} X 10"+add_tags('sup',power1)
            else:
                pr=round(pr,3) 

            if not  ((sc>=1 and sc<=10000) or (round(sc,3)!=0 and round(sc,3)!=0.001)):
                base1,power1=Roundoff(sc)
                sc=f"{base1} X 10"+add_tags('sup',power1)
            else:
                sc=round(sc,3) 
            
            if not ( (fts>=1 and fts<=10000) or (round(fts,3)!=0 and round(fts,3)!=0.001)):
                base1,power1=Roundoff(fts)
                fts=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                fts=round(fts,3)
       
            if not  ((frst>=1 and frst<=10000) or (round(frst,3)!=0 and round(frst,3)!=0.001)):
                base1,power1=Roundoff(frst)
                frst=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst=round(frst,3) 
    
            if not  ((ans>=1 and ans<=10000) or (round(ans,4)!=0 and round(ans,4)!=0.001)):
                base1,power1=Roundoff(ans)
                ans=f"{base1} X 10"+add_tags('sup',power1)
            else:
                ans=round(ans,4) 

            if not  ((total>=1 and total<=10000) or (round(total,4)!=0 and round(total,4)!=0.001)):
                base1,power1=Roundoff(total)
                total=f"{base1} X 10"+add_tags('sup',power1)
            else:
                total=round(total,4) 

            if not  ((frst1>=1 and frst1<=10000) or (round(frst1,3)!=0 and round(frst1,3)!=0.001)):
                base1,power1=Roundoff(frst1)
                frst1=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst1=round(frst1,3) 

            if not  ((frst2>=1 and frst2<=10000) or (round(frst2,3)!=0 and round(frst2,3)!=0.001)):
                base1,power1=Roundoff(frst2)
                frst2=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst2=round(frst2,3) 
           

             

            context={
                'ftr':ftr,
                'frst':frst,
                'frst1':frst1,
                'frst2':frst2,
                'fsc':fsc,
                'fts':fts,
                'tr':tr,
                'pr':pr,
                'sc':sc,
                'cc':cc,
                'tr1':tr1,
                'pr1':pr1,
                'sc1':sc1,
                'x':x,
                'ans2':ans2,
                'y':y,
                'an':an,
                'total':total,
                'values':values,
                
              
                
                'ans':ans,
                
                'given_data':given_data,
                }

                 
       
            return render(request,'PROBABILITY/binomial-probability-calculator.html',context)

        if given_data=="form5" and tr and pr and sc:

            #copy the values:
            tr1 = tr
            pr1 = pr
            sc1 = sc            

            #calculations
            cc = sc+1
            ftr = math.factorial(tr)
            fsc = math.factorial(sc)
            fts = math.factorial(tr-sc)
            frst = (ftr/(fsc*fts))
            frst1 = (pr**sc)
            frst2 = ((1-pr)**(tr-sc))
            

            
            ans = frst*frst1*frst2
            an = {}
            
           
            for y in range(sc , tr+1 ):
                an[str(y)] = round(ftr/(math.factorial(y)*(math.factorial(abs(tr-y))))*(pr**y)*((1-pr)**(abs(y-tr))),4)
            values = an.values()
            total = sum(values)
               
            
            ans2={}
            for x in range(0, tr+1):
                ans2[str(x)] = round(ftr/(math.factorial(x)*(math.factorial(abs(tr-x))))*(pr**x)*((1-pr)**(abs(x-tr))),4)
            #print(ans2)
            #round Off
            if not ( (tr>=1 and tr<=10000) or (round(tr,3)!=0 and round(tr,3)!=0.001)):
                base1,power1=Roundoff(tr)
                tr=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                tr=round(tr,3)
       
            if not  ((pr>=1 and pr<=10000) or (round(pr,3)!=0 and round(pr,3)!=0.001)):
                base1,power1=Roundoff(pr)
                pr=f"{base1} X 10"+add_tags('sup',power1)
            else:
                pr=round(pr,3) 

            if not  ((sc>=1 and sc<=10000) or (round(sc,3)!=0 and round(sc,3)!=0.001)):
                base1,power1=Roundoff(sc)
                sc=f"{base1} X 10"+add_tags('sup',power1)
            else:
                sc=round(sc,3) 
            
            if not ( (fts>=1 and fts<=10000) or (round(fts,3)!=0 and round(fts,3)!=0.001)):
                base1,power1=Roundoff(fts)
                fts=f"{base1} X 10 "+add_tags('sup',power1)
            else:
                fts=round(fts,3)
       
            if not  ((frst>=1 and frst<=10000) or (round(frst,3)!=0 and round(frst,3)!=0.001)):
                base1,power1=Roundoff(frst)
                frst=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst=round(frst,3) 

            if not  ((total>=1 and total<=10000) or (round(total,4)!=0 and round(total,4)!=0.001)):
                base1,power1=Roundoff(total)
                total=f"{base1} X 10"+add_tags('sup',power1)
            else:
                total=round(total,4) 
    
            if not  ((ans>=1 and ans<=10000) or (round(ans,4)!=0 and round(ans,4)!=0.001)):
                base1,power1=Roundoff(ans)
                ans=f"{base1} X 10"+add_tags('sup',power1)
            else:
                ans=round(ans,4) 

            if not  ((frst1>=1 and frst1<=10000) or (round(frst1,3)!=0 and round(frst1,3)!=0.001)):
                base1,power1=Roundoff(frst1)
                frst1=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst1=round(frst1,3) 

            if not  ((frst2>=1 and frst2<=10000) or (round(frst2,3)!=0 and round(frst2,3)!=0.001)):
                base1,power1=Roundoff(frst2)
                frst2=f"{base1} X 10"+add_tags('sup',power1)
            else:
                frst2=round(frst2,3) 
           

             

            context={
                'ftr':ftr,
                'frst':frst,
                'frst1':frst1,
                'frst2':frst2,
                'fsc':fsc,
                'fts':fts,
                'tr':tr,
                'pr':pr,
                'sc':sc,
                'tr1':tr1,
                'pr1':pr1,
                'sc1':sc1,
                'x':x,
                'y':y,
                'an':an,
                'total':total,
                'values':values,
                'cc':cc,
                'ans2':ans2,
                
              
                
                'ans':ans,
                
                'given_data':given_data,
                }

                 
       
            return render(request,'PROBABILITY/binomial-probability-calculator.html',context)
        else:
            return render(request,'PROBABILITY/binomial-probability-calculator.html',{'given_data':given_data})
            
    else: 
        return render(request,'PROBABILITY/binomial-probability-calculator.html',{'given_data':'form1'})
def chebyshevs_theorem_calculator(request):
    if request.method=="POST":
        f_unit=request.POST['f_type']
        a=request.POST['a']
        b=request.POST['b']
        if(f_unit=="one"):
            d=(int(b)/int(a))*100
        else:
            d=(1/(int(a)**2))*100
        return render(request, 'PROBABILITY/chebyshevs-theorem-calculator.html', context={'a': a,"b":b,"d":d,"f_unit":f_unit})
    return render(request, 'PROBABILITY/chebyshevs-theorem-calculator.html',context={'a': 5,"b":5})



def fact(n):
     
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res

def count_heads(n, r):
     
    output = fact(n) / (fact(r) * fact(n - r))
    output = output / (pow(2, n))
    return output




def coin_flip_probability_calculator(request):
    try:
        if request.method=="POST":
            
            Given=request.POST.get("Given")
            n=request.POST.get("n")
            if request.POST.get("n"):
                n_calculated=int(request.POST.get("n"))
            k=request.POST.get("k")
            if request.POST.get("k"):
                k_calculated=int(request.POST.get("k"))
            p=0.5
            r_values=range(0,n_calculated)
            data_binom = [binom.pmf(r, n_calculated, p) for r in r_values ]
            if Given=="at_most" and k and n:
                string1=""
                if k_calculated<=n_calculated:
                    result=sum(data_binom[0:k_calculated])/sum(data_binom)
                    #+ "+"<sup>"+str(n_calculated)+"</sup>C<sub>1 ......."
                    string1="<sup>"+str(n_calculated)+"</sup>C<sub>0</sub> p<sup>0</sup>(1-p)<sup>"+str(n_calculated)+"</sup>  +"+"<sup>"+str(n_calculated)+"</sup>C<sub>1</sub> p<sup>1</sup>(1-p)<sup>"+str(n_calculated-1)+"</sup> + ......."+"<sup>"+str(n_calculated)+"</sup>C<sub>"+str(k_calculated)+"</sub> p<sup>"+str(k_calculated)+"</sup>(1-p)<sup>"+str(n_calculated-k_calculated)+"</sup>  "                
                    p=str(round(result*100,2))+"%"
                    context={
                        "Given":Given,
                        "n":n,
                        "k":k,
                        "n_calculated":n_calculated,
                        "k_calculated":k_calculated,
                        "result":result,
                        "p":p,
                        "string1":string1,
                        "id":1
                    }
                else:
                    messages.error(request,"Value of k should be less than or equal to n")
                    return render(request,'PROBABILITY/coin-flip-probability-calculator.html')
                return render(request,"PROBABILITY/coin-flip-probability-calculator.html",context)
            elif Given=="exactly" and k and n:
                if k_calculated<=n_calculated:
                    result=data_binom[k_calculated]/sum(data_binom)
                    string1="<sup>"+str(n_calculated)+"</sup>C<sub>"+str(k_calculated)+"</sub> p<sup>"+str(k_calculated)+"</sup>(1-p)<sup>"+str(n_calculated-k_calculated)+"</sup>  "                
                    p=str(round(result*100,2))+"%"
                    context={
                        "Given":Given,
                        "n":n,
                        "k":k,
                        "n_calculated":n_calculated,
                        "k_calculated":k_calculated,
                        "result":result,
                        "p":p,
                        "string1":string1,
                        "id":1
                    }
                    return render(request,"PROBABILITY/coin-flip-probability-calculator.html",context)
                else:
                    messages.error(request,"Value of k should be less than or equal to n")
                    return render(request,'PROBABILITY/coin-flip-probability-calculator.html')
            elif Given=="at_least" and k and n:
                if k_calculated<=n_calculated:
                    result=sum(data_binom[k_calculated:])/sum(data_binom)
                    string1="<sup>"+str(n_calculated)+"</sup>C<sub>"+str(k_calculated)+"</sub> p<sup>"+str(k_calculated)+"</sup>(1-p)<sup>"+str(n_calculated-k_calculated)+"</sup> +"+"<sup>"+str(n_calculated)+"</sup>C<sub>"+str(k_calculated+1)+"</sub> p<sup>"+str(k_calculated+1)+"</sup>(1-p)<sup>"+str(n_calculated-k_calculated-1)+"</sup>  +............."+str(n_calculated)+"</sup>C<sub>"+str(n_calculated)+"</sub> p<sup>"+str(0)+"</sup>(1-p)<sup>"+str(n_calculated)+"</sup>  "                                               
                    p=str(round(result*100,2))+"%"
                    context={
                        "Given":Given,
                        "n":n,
                        "k":k,
                        "n_calculated":n_calculated,
                        "k_calculated":k_calculated,
                        "result":result,
                        "p":p,
                        "string1":string1,
                        "id":1
                    }
                    return render(request,"PROBABILITY/coin-flip-probability-calculator.html",context)
                else:
                    messages.error(request,"Value of k should be less than or equal to n")
                    return render(request,'PROBABILITY/coin-flip-probability-calculator.html')
            if Given=="equal_to" and k and n:
                
                context={
                    "Given":Given,
                    "n":"",
                    "k":"",
                    
                }
                return render(request,"PROBABILITY/coin-flip-probability-calculator.html",context)
        else:
            return render(request,"PROBABILITY/coin-flip-probability-calculator.html",{"n":5,"k":3})
    except:
        return render(request,"PROBABILITY/coin-flip-probability-calculator.html",{"n":5,"k":2})
def check_decimal_values(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

def sensitivity_and_specificity_calculator(request):
    
    
    if request.method == "POST":
        tp = check_decimal_values(request.POST.get('tp'))
        tn = check_decimal_values(request.POST.get('tn'))
        fp = check_decimal_values(request.POST.get('fp'))
        fn = check_decimal_values(request.POST.get('fn'))
        
        Sensitivity = round((tp/(tp+fn)),4)
        Specificity = round((tn/(fp+tn)),4)
        
        d={'sensitivity':Sensitivity,'specificity':Specificity,'tp':tp,'tn':tn,'fp':fp,'fn':fn,'id':1}
        return render(request, "PROBABILITY/sensitivity-and-specificity-calculator.html",d)
        
    else:
        d={'sensitivity':0.5,'Specificity':0.5,'tp':1,'tn':1,'fp':1,'fn':1}
        return render(request, "PROBABILITY/sensitivity-and-specificity-calculator.html",d)



def coin_toss_probability_calculator(request):
    
   
    if request.method=='POST':
        
        num1=request.POST.get("a")
        num2=request.POST.get("b")
        try:
            num1=int(num1)
            num2=int(num2)
            if num1<num2:
                messages.error(request,"Number of tosses value should be greater than number of heads/tails")
                return render(request,'PROBABILITY/coin-toss-probability-calculator.html',{'input1':num1,'input2':num2,'go_tag':'#coin_toss'})
            else:
                total_o=2**num1
                l=[i for i in range(1,num1+1)]
                fav=combinations(l,num2)
                count=0
                for i in fav:
                    count+=1
                pr=count/total_o
                result={
                    "pr":pr,
                    "total":total_o,
                    "fav":count,
                    "num1":num1,
                    "num2":num2,
                    'id':1

                }
                return render(request,'PROBABILITY/coin-toss-probability-calculator.html',result)
        except:
            messages.error(request,"Enter a valid input")
            return render(request,'PROBABILITY/coin-toss-probability-calculator.html',{'num1':num1,'num2':num2,"id":1})
    else:
        
        return render(request, "PROBABILITY/coin-toss-probability-calculator.html",{'num1':5,'num2':2})     

def combinations_calculator(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        description={}
        if(int(a)<1 or int(b)<1 or int(a)<int(b)):
            messages.info(request,"Invalid Value")
        else:
            description['l1_bold']="C(n,r) = n!/(r!(n-r)!)"
            description['l2']="where C is the number of combinations;"
            description['l3']="n is the total number of elements in the set; and"
            description['l4']="r is the number of elements you choose from this set"
            c=(math.factorial(int(a))/(math.factorial(int(a)-int(b))*math.factorial(int(b))))
            description['l5'] = "Combination without repitition = "+str(c)
            d=(math.factorial(int(b)+int(a)-1)/(math.factorial(int(a)-1)*math.factorial(int(b))))
            description['l6'] = "Combination with repitition = " + str(d)
            return render(request, 'PROBABILITY/combinations-calculator.html',context={'a':a,'b':b,"c":int(c),"d":int(d),"answer":description,"id":1})
    return render(request, 'PROBABILITY/combinations-calculator.html',context={'a':5,'b':1})
   




def cumulative_probability_calculator(request):
    errors = []
    
    if request.method == 'POST':
        # get url that the user has entered
        try:
        
            data1 = request.POST.get('data1')
            data2 = request.POST.get('data2')
            
            
        except:
            errors.append(
                "Unable to get necessary input, please try again."
            )

        data3 = [b for i in data1.split(',') for a in i.split(' ') for b in a.split('\t') if len(b)>0]
        data2 = [b for i in data2.split(',') for a in i.split(' ') for b in a.split('\t') if len(b)>0]

        
        
        try:
            data2 = [int(i) for i in data2]
        except ValueError: 
            return "ERROR: There are non-numeric elements!"


        

        v = []
        sum=0
        for num in data2:
            sum=sum+num
            v.append(sum)
        

        
        data = zip(data3,data2,v)

        data2 = str(data2)[1:-1] 
        
        context = {
            'id':1,
            'data1':data1,
            'data2':data2,
            'errors':errors,
            'data':data,
        }
                    
                

        # # print(datarange)
        # # print(min_element)
        # # print(max_element)
        return render(request,'PROBABILITY/cumulative-probability-calculator.html',context)
    
    data1 = "2-10 11-19 20-28"
    data2 = "1 3 9"

    context = {
            
            'data1':data1,
            'data2':data2,
        }
    return render(request,'PROBABILITY/cumulative-probability-calculator.html',context)

def numRollsToTarget( d, f, target):
    dp = [1] + [0]*target
    for i in range(d):
        for j in range(target, -1, -1):
            dp[j] = sum([dp[j-k] for k in range(1, 1+min(f, j))] or [0])
    return dp[target] 
def dice_probability_calculator(request):

    if request.method=='POST':
        if "f1" in request.POST:
            selectdice = request.POST.get('selectdice')

            noofdice = request.POST.get('noofdice')
            gamerule = request.POST.get('gamerule')
            valueondice = request.POST.get('valueondice')

            if gamerule[0]== '1':
                k=pow(int(selectdice),int(noofdice))
                probability=1/k
                context = {
                    'k' : k,
                    'no_of_outcome':1,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '2':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = pow((int(selectdice)-int(valueondice)+1),int(noofdice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '3':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = pow((int(valueondice)),int(noofdice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '4':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = numRollsToTarget( int(noofdice), int(selectdice), int(valueondice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '5':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = 0
                max_sum = int(selectdice)*int(noofdice)
                p = int(valueondice)
                for sum in range(p,max_sum+1):
                    no_of_outcome+=numRollsToTarget( int(noofdice), int(selectdice), sum)
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '6':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = 0
                p=int(valueondice)
                for sum in range(1,p+1):
                    no_of_outcome+=numRollsToTarget( int(noofdice), int(selectdice), sum)
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            
            return render(request,'PROBABILITY/dice-probability-calculator.html',context)
        else:
            gamerule = request.POST.get('gamerule')
            selectdice = request.POST.get('selectdice')
            noofdice = request.POST.get('noofdice')
            valueondice = request.POST.get('valueondice')
            id1 = 0
            if len(gamerule)!=0:
                if gamerule[0] == '7':
                    id1=7
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'id1':id1
                    }
                    return render(request,'PROBABILITY/dice-probability-calculator.html',context)
                if gamerule[0] == '8':
                    id1=8
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'id1':id1
                    }
                    return render(request,'PROBABILITY/dice-probability-calculator.html',context)
                else:
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'selectdice':str(selectdice),
                        'gamerule':str(gamerule)
                    }
                    return render(request,'PROBABILITY/dice-probability-calculator.html',context)
            else:
                selectdice = request.POST.get('selectdice')
                context = {
                    'noofdice':str(noofdice),
                    'valueondice':str(valueondice),
                    'selectdice':str(selectdice)
                }
                return render(request,'PROBABILITY/dice-probability-calculator.html',context)



                

                
        

        
    else:
        d = {'noofdice':1,'valueondice':3,
                    'selectdice':2,}
        
        return render(request,'PROBABILITY/dice-probability-calculator.html',d)

def empirical_probability_calculator(request):
    if request.method == "POST":
        f = request.POST.get('number_of_times_event_occurs')
        n = request.POST.get('number_of_times_experiment_performed')
        empirical_probab = round(int(f) / int(n),4)

        context = {
            'number_of_times_event_occurs':f,
            'number_of_times_experiment_performed':n,
            'empirical_probab': empirical_probab,
            'id':1
        }
        return render(request, "PROBABILITY/empirical-probability-calculator.html", context)
    else:
        d = {'number_of_times_event_occurs':4,'number_of_times_experiment_performed':2}
        return render(request, "PROBABILITY/empirical-probability-calculator.html",d)


def expected_value(values, probabilities):
    return sum([v * p for v, p in zip(values, probabilities)])

def expected_value_calculator(request):

    
    errors = []
    
    if request.method == 'POST':
        # get url that the user has entered
        try:
        
            data1 = request.POST.get('data1')
            data2 = request.POST.get('data2')
            
        except:
            errors.append(
                "Unable to get necessary input, please try again."
            )

        data1 = [b for i in data1.split(',') for a in i.split(' ') for b in a.split('\t') if len(b)>0]
        data2 = [b for i in data2.split(',') for a in i.split(' ') for b in a.split('\t') if len(b)>0]
        try:
            data1 = [float(i) for i in data1]
            data2 = [float(i) for i in data2]
        except ValueError: 
            return "ERROR: There are non-numeric elements!"

        sum = 0.0
        for i in data2:
            sum=sum+i

       
        if sum != 1.0:
            errors.append("Sum of all probability is not equal to one")
            context = {
                'errors':errors,
                'id':1,
            }
        elif len(data1)!=len(data2):
            errors.append("Length of Both rondom variable array and Probability of random variable is not equal")
            context = {
                'data1':data1,
                'data2':data2,
                'errors':errors,
                'id':1,
            }
        else:
            k = expected_value(data1, data2)
            results=k

            context = {
                'data1':data1,
                'data2':data2,
                'results':results,
                'id':1
            }
           
        return render(request,'PROBABILITY/expected-value-calculator.html',context)

    else:
        
        context = {
        
        'results':"0",
        'id':1
        }
        
        
        return render(request,'PROBABILITY/expected-value-calculator.html',context)

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 

cards = {'black': 26,
            'red':26,
            'heart':13,
            'diamond':13,
            'spade':13,
            'club':13,
            'jack':4,
            'queen':4,
            'king':4,
            'ace':4,
            'facecard':16 }

def prob(no,card_name):
    total_cards = cards[card_name]
    #prob1 = ncr(52,no)
    #prob2 = ncr(total_cards,no)
    probability = ncr(total_cards,no) / ncr(52,no)
    return round(probability,3)
def deck_of_cards_probability_calculator(request):
    if request.method == "POST":
        cards_drawn = int(request.POST.get('cards_drawn'))
        #card_name = request.POST.get('card to be drawn')
        card_name = request.POST.get('drop')
        
    
        if card_name==None:
            
            messages.error(request, "Please select one option")
            return render(request, "PROBABILITY/deck-of-cards-probability-calculator.html")
        else:
            probability = prob(cards_drawn,card_name)
            nE = ncr(cards[card_name],cards_drawn)
            nS = ncr(52,cards_drawn)
            total_cards = cards[card_name]
            context = {
                'cards_drawn':cards_drawn,
                'card_name':card_name,
                'probability':probability,
                'nE':nE,
                'nS':nS,
                'total_cards':total_cards,
                'id':1
            }
            return render(request, "PROBABILITY/deck-of-cards-probability-calculator.html", context)
    else:
        return render(request, "PROBABILITY/deck-of-cards-probability-calculator.html")


def dependent_probability_calculator(request):
    if request.method == "POST":
        a1 = (request.POST.get('a1'))
        a22 = (request.POST.get('a22'))
        c1 = (request.POST.get('c1'))
        a1 = int(a1)
        a22 = int(a22)
        
        f = 0
        
        if c1 == 0 or c1==None:
            
            c = a1+a22
            d = (a1/c)*((a1-1)/(c-1))
            e = (a22/c)*((a22-1)/(c-1))
        else:
            c1 = int(c1)
            c = a1+a22+c1
            d = (a1/c)*((a1-1)/(c-1))*((a1-2)/(c-2))
            e = (a22/c)*((a22-1)/(c-1))*((a22-2)/(c-2))
            f = (c1/c)*((c1-1)/(c-1))*((c1-2)/(c-2))
        context = {
            'a1': a1, 'a22': a22, 'd': d, 'e': e, 'c': c, 'c1': c1, 'f': f,
            'id': 1,
        }

        return render(request, "PROBABILITY/dependent-probability-calculator.html", context)
    else:
        d = {'a1': 5, 'a22': 4,'c1': 0}
        return render(request, "PROBABILITY/dependent-probability-calculator.html", d)




def dice_roll_probability_calculator(request):

    if request.method=='POST':
        if "f1" in request.POST:
            selectdice = request.POST.get('selectdice')

            noofdice = request.POST.get('noofdice')
            gamerule = request.POST.get('gamerule')
            valueondice = request.POST.get('valueondice')

            if gamerule[0]== '1':
                k=pow(int(selectdice),int(noofdice))
                probability=1/k
                context = {
                    'k' : k,
                    'no_of_outcome':1,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '2':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = pow((int(selectdice)-int(valueondice)+1),int(noofdice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '3':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = pow((int(valueondice)),int(noofdice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '4':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = numRollsToTarget( int(noofdice), int(selectdice), int(valueondice))
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            if gamerule[0]== '5':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = 0
                max_sum = int(selectdice)*int(noofdice)
                p = int(valueondice)
                for sum in range(p,max_sum+1):
                    no_of_outcome+=numRollsToTarget( int(noofdice), int(selectdice), sum)
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                

            if gamerule[0]== '6':
                k=pow(int(selectdice),int(noofdice))
                no_of_outcome = 0
                p=int(valueondice)
                for sum in range(1,p+1):
                    no_of_outcome+=numRollsToTarget( int(noofdice), int(selectdice), sum)
                probability=no_of_outcome/k
                context = {
                    'k' : k,
                    'no_of_outcome':no_of_outcome,
                    'probability' : probability,
                    # 'max': max,
                    # 'classes':classes,
                    # 'classwidth' : classwidth,
                    'id':1
                }
                
            
            return render(request,'PROBABILITY/dice-roll-probability-calculator.html',context)
        else:
            gamerule = request.POST.get('gamerule')
            selectdice = request.POST.get('selectdice')
            noofdice = request.POST.get('noofdice')
            valueondice = request.POST.get('valueondice')
            id1 = 0
            if len(gamerule)!=0:
                if gamerule[0] == '7':
                    id1=7
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'id1':id1
                    }
                    return render(request,'PROBABILITY/dice-roll-probability-calculator.html',context)
                if gamerule[0] == '8':
                    id1=8
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'id1':id1
                    }
                    return render(request,'PROBABILITY/dice-roll-probability-calculator.html',context)
                else:
                    context = {
                        'noofdice':str(noofdice),
                        'valueondice':str(valueondice),
                        'selectdice':str(selectdice),
                        'gamerule':str(gamerule)
                    }
                    return render(request,'PROBABILITY/dice-roll-probability-calculator.html',context)
            else:
                selectdice = request.POST.get('selectdice')
                context = {
                    'noofdice':str(noofdice),
                    'valueondice':str(valueondice),
                    'selectdice':str(selectdice)
                }
                return render(request,'PROBABILITY/dice-roll-probability-calculator.html',context)



                

                
        

        
    else:
        d = {'no-of-dice':1}
        return render(request,'PROBABILITY/dice-roll-probability-calculator.html',d)

def discrete_probability_distribution_calculator(request):
  return render(request, 'PROBABILITY/discrete-probability-distribution-calculator.html')

def experimental_probability_calculator(request):
    if request.method == 'POST':
        n=request.POST.get("n")
        r=request.POST.get("r")
        print(n,r)
        prob=float(n)/float(r)
        return render(request, 'PROBABILITY/experimental-probability-calculator.html',{"n":n,"r":r,"prob":prob,"id":1})
    else:
        return render(request, 'PROBABILITY/experimental-probability-calculator.html',{"n":4,"r":5})


def exponential_probability_calculator(request):
    if request.method == 'POST':
        given_data = request.POST.get('given_data')
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('pm')!=None and request.POST.get('pm')!='' :
            inp=str(request.POST.get('pm'))
            if inp.isdigit(): 
                pm=int(request.POST.get('pm'))
            else:
                pm=float(request.POST.get('pm'))
        else:
            pm=None
        
        if request.POST.get('tt')!=None and request.POST.get('tt')!='' :
            inp=str(request.POST.get('tt'))
            if inp.isdigit(): 
                tt=int(request.POST.get('tt'))
            else:
                tt=float(request.POST.get('tt'))
        else:
            tt=None

        if request.POST.get('tw')!=None and request.POST.get('tw')!='' :
            inp=str(request.POST.get('tw'))
            if inp.isdigit(): 
                tw=int(request.POST.get('tw'))
            else:
                tw=float(request.POST.get('tw'))
        else:
            tw=None

        if request.POST.get('lt')!=None and request.POST.get('lt')!='' :
            inp=str(request.POST.get('lt'))
            if inp.isdigit(): 
                lt=int(request.POST.get('lt'))
            else:
                lt=float(request.POST.get('lt'))
        else:
            lt=None

        if request.POST.get('rt')!=None and request.POST.get('rt')!='' :
            inp=str(request.POST.get('rt'))
            if inp.isdigit(): 
                rt=int(request.POST.get('rt'))
            else:
                rt=float(request.POST.get('rt'))
        else:
            rt=None
        
        if given_data == "form1" and pm and tt and tw:

            ans = round((math.exp(-tt/pm) - math.exp(-tw/pm)),4)
           


            context = {
                'pm':pm,
                'tt':tt,
                'tw':tw,
                'lt':lt,
                'rt':rt,
                'ans':ans,
                'id':1,
                'given_data':given_data
            }
            return render(request,"PROBABILITY/exponential-probability-calculator.html", context) 

        if given_data == "form2" and pm and lt:

            ans = round((1 - math.exp(-lt/pm)),4)
           

            context = {
                'pm':pm,
                'lt':lt,
                'tw':tw,
                'lt':lt,
                'rt':rt,
                'ans':ans,
                'id':1,
                'given_data':given_data
                }
            return render(request,"PROBABILITY/exponential-probability-calculator.html", context) 

        if given_data == "form3" and pm and rt:

            ans = round((math.exp(-rt/pm)),4)
           
           

            context = {
                'pm':pm,
                'rt':rt,
                'tw':tw,
                'lt':lt,
                'rt':rt,
                'ans':ans,
                'id':1,
                'given_data':given_data
                }
            return render(request,"PROBABILITY/exponential-probability-calculator.html", context) 

        else:
            return render(request,"PROBABILITY/exponential-probability-calculator.html",{'given_data':given_data})
    else: 
        return render(request,'PROBABILITY/exponential-probability-calculator.html',{'given_data':'form1'})



def cal_distribution_prob(p,k):
    return round(p*((1-p)**(k-1)),4)

def geometric_probability_calculator(request):
    if request.method == "POST":
        success_prob = request.POST.get('success_prob')
        k_trails = request.POST.get('k_trails')
        probability = cal_distribution_prob(float(success_prob),int(k_trails))
                
        
        context = {
            'success_prob' : success_prob,
            'k_trails': k_trails,
            #'classes':classes,
            'probability' : probability,
            'id':1
        }
        return render(request, "PROBABILITY/geometric-probability-calculator.html", context)
    else:
        d = {'success_prob':0.25,'k_trails':4}
        return render(request, "PROBABILITY/geometric-probability-calculator.html",d)
def independent_probability_calculator(request):
    if request.method == "POST":
        a1 = (request.POST.get('a1'))
        a22 = (request.POST.get('a22'))
        c1 = (request.POST.get('c1'))
        a1 = int(a1)
        a22 = int(a22)
       
        
        f = 0
        if c1 == "":
            c = a1+a22
            d = (a1/c)*((a1)/(c))
            e = (a22/c)*((a22)/(c))
        else:
            c1 = int(c1)
            c = a1+a22+c1
            d = (a1/c)*((a1)/(c))*((a1)/(c))
            e = (a22/c)*((a22)/(c))*((a22)/(c))
            f = (c1/c)*((c1)/(c))*((c1)/(c))
        context = {
            'a1': a1, 'a22': a22, 'd': d, 'e': e, 'c': c, 'c1': c1, 'f': f,
            'id': 1,
        }

        return render(request, "PROBABILITY/independent-probability-calculator.html", context)
    else:
        d = {'a1': 5, 'a22': 5,"c1":1}
        return render(request, "PROBABILITY/independent-probability-calculator.html", d)

def labor_probability_calculator(request):
  return render(request, 'PROBABILITY/labor-probability-calculator.html')
def life_expectancy_probability_calculator(request):
  return render(request, 'PROBABILITY/life-expectancy-probability-calculator.html')


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer

        
def lottery_probability_calculator(request):
    if request.method == "POST":
        m = (request.POST.get('m'))
        n = (request.POST.get('n'))
        t = (request.POST.get('t'))
        m1 = int(m)
        n1 = int(n)
        t1 = int(t)
        f = ncr(t1, m1)/(ncr(m1, n1)*ncr(t1-m1, m1-n1))
        context = {
            'f': f,
            'm1': m1,
            'n1': n1,
            't1': t1,
            'id': 1
        }
        return render(request, "PROBABILITY/lottery-probability-calculator.html", context)
    else:
        d = {'t': 0}
        return render(request, "PROBABILITY/lottery-probability-calculator.html", d)
def mean_of_probability_distribution_calculator(request):
    
    if request.method == "POST":
        di={"id":0,"sum":0,"l":[],"val":0,"nu":0}
        nu = request.POST.get('nu')       
        prob=0
        data=[]
        ans={}
        count=0
        for i in range(int(nu)):
            d=check_decimal_values(request.POST.get('r'+str(i)))
            p=check_decimal_values(request.POST.get('s'+str(i)))
            data.append(d*p)
            prob+=p
            ans["d{0}".format(i)] = d
            ans["p{0}".format(i)] = p
            di["d{0}".format(i)] = d
            di["p{0}".format(i)] = p
            count+=1
            
        di["nu"]=nu 
        di["id"]=1
        di["l"]=ans
        di["val"]=str(count)
        
        if prob==1:
            for i in range(len(data)):
                di["m{0}".format(i)] = data[i]
            
            di["sum"]=sum(data)
            
        else:
            di["sum"]="Sum of Probability Distribution must be 1 "
        
        return render(request,'PROBABILITY/mean-of-probability-distribution-calculator.html',dict(di))
    else:
        di={ 'id':0, 'nu':0}
        return render(request,'PROBABILITY/mean-of-probability-distribution-calculator.html',dict(di))

def odds_calculator(request):
    if request.method=='POST':
        num1=request.POST.get("input1")
        num2=request.POST.get("input2")
        num3=request.POST.get("input3")
        try:
            try:
                n1=int(num1)
            except:
                n1=float(num1)
            try:
                n2=int(num2)
            except:
                n2=float(num2)
            pa=round(n1/(n1+n2),4)
            pb=round(n2/(n1+n2),4)
            pa_p=round(pa*100,2)
            pb_p=round(pb*100,2)
            from fractions import Fraction
            if int(n1)==int(n2):
                f1='1 : 1'
            elif int(n1)>int(n2):
                g1=Fraction(int(n1),int(n2))
                g2=str(g1).split('/')
                if num3=="for winning":
                    f1='{} : {}'.format(g2[0],g2[1])
                else:
                    f1='{} : {}'.format(g2[1],g2[0])
            elif int(n1)<int(n2):
                g1=Fraction(int(n2),int(n1))
                g2=str(g1).split('/')
                if num3=="for winning":
                    f1='{} : {}'.format(g2[1],g2[0])
                else:
                    f1='{} : {}'.format(g2[0],g2[1])
          
            v=[]
            a=v.append
            a('<p>For <strong>{} to {} odds</strong> {}:</p>'.format(num1,num2,num3))
            a('<p><strong>Probability of:</strong></p>')
            if num3=="for winning":
                a('<p>Winning = {} or {}%</p>'.format(pa,pa_p))
                a('<p>Losing = {} or {}%</p>'.format(pb,pb_p))
            else:
                a('<p>Winning = {} or {}%</p>'.format(pb,pb_p))
                a('<p>Losing = {} or {}%</p>'.format(pa,pa_p))
            a('<p>Odds {} = {}</p>'.format(num3,f1))
            result=''.join(v)
            context={'input1':num1,'input2':num2,'input3':num3,'detailStep':result,'go_tag':'#odds_probability'}
            return render(request,'PROBABILITY/odds-calculator.html',context)
        except:
            messages.error(request,"Enter a valid input")
            context={'input1':num1,'input2':num2,'input3':num3}
            return render(request,'PROBABILITY/odds-calculator.html',context)
    else:
	    return render(request,'PROBABILITY/odds-calculator.html')



def options_probability_calculator(request):
  return render(request, 'PROBABILITY/options-probability-calculator.html')
def percentage_probability_calculator(request):
  return render(request, 'PROBABILITY/percentage-probability-calculator.html')

def permutations(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        description={}
        if(int(a)<1 or int(b)<1):
            messages.info(request,"Invalid Value")
        else:
            description['l1_bold']="P(n,r) = n!/(n-r)!"
            description['l2']="where p is the number of permutations;"
            description['l3']="n is the total number of elements in the set; and"
            description['l4']="r is the number of elements you choose from this set"
            c=(math.factorial(int(a))/math.factorial(int(a)-int(b)))
            description['l5'] = "Permutation without repitition = "+str(c)
            d=int(a)**int(b)
            description['l6'] = "Permutation with repitition = " + str(d)
            return render(request, 'PROBABILITY/permutations.html',context={'a':a,'b':b,"c":int(c),"d":int(d),"answer":description})
    return render(request, 'PROBABILITY/permutations.html')
def poisson_probability_calculator(request):
    if request.method=="POST":
        try:
            n = int(request.POST['n'])
            l = int(request.POST['l'])

            e =  2.718282

            res = pow(l,n) / (math.factorial(n)*pow(e,l))

            #return HttpResponse(res)

            ln = [x for x in range(n+1)]

            first = round(1/pow(e,l),3)

            exact = [first]
            cum = [first]
            
            for i in range(1,n+1):
                #return HttpResponse(str(l)+str(i))
                val = round(pow(l,i) / (math.factorial(i)*pow(e,l)),4)
                exact.append(val)
                cum.append(round(exact[i]+cum[i-1],4))

            res = exact[-1]
            cres = cum[-1]
            notres = abs(1-cres)

            exact = [str(x)[:-1] for x in exact]
            cum = [str(x)[:-1] for x in cum]

            

            res_table = zip(ln,exact,cum)

            context={
                'go_to':"#result",
                'result':True,
                'res_table':res_table,
                'n':str(n),
                'l':str(l),
                'res':round(res,3),
                'notres':round(notres,3),
                'cres':round(cres,3),
            }

            return render(request,'PROBABILITY/poisson-probability-calculator.html',context)

        except:
            context={
                'error':True,
                'n':str(n),
                'l':str(l),
            }
            return render(request,'PROBABILITY/poisson-probability-calculator.html',context)

    return render(request,'PROBABILITY/poisson-probability-calculator.html')

def poker_probability_calculator(request):
  return render(request, 'PROBABILITY/poker-probability-calculator.html')

def probability_calculator(request):
    if request.method=="POST":
        a=float(request.POST['n'])
        b=float(request.POST['r'])
        if(a<0 or b<0) or a<b:
            messages.info(request,"invalid value")
        prob=b/a
        return render(request, 'PROBABILITY/probability-calculator.html',context={"n":a,"r":b,"prob":prob,"id":1})
    return render(request, 'PROBABILITY/probability-calculator.html')


def probability_density_function_calculator(request):
    errors = []
    if request.method=='POST':
        try:
            normalrandomvariable = request.POST.get('normalrandomvariable')
            mean = request.POST.get('mean')
            standarddeviation = request.POST.get('standarddeviation')
        except:
            errors.append(
                "Unable to get necessary input, please try again."
            )
        try:
            normalrandomvariable = float(normalrandomvariable)
            mean = float(mean)
            standarddeviation = float(standarddeviation) 
        except ValueError: 
            return "ERROR: There are non-numeric elements!"

        result = (1.0 / (standarddeviation * math.sqrt(2*math.pi))) * math.exp(-0.5*((normalrandomvariable - mean) / standarddeviation) ** 2)

        context = {
                'id':1,
                'normalrandomvariable':normalrandomvariable,
                'mean':mean,
                'standarddeviation':standarddeviation,
                'result':result,
                'errors':errors
            }
        

        return render(request,'PROBABILITY/probability-density-function-calculator.html',context)
    return render(request,'PROBABILITY/probability-density-function-calculator.html',{'normalrandomvariable':10,
                'mean':10,
                'standarddeviation':10})
def probability_distribution_calculator(request):
    if request.method == 'POST':
        given_data = request.POST.get('given_data')
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('nu')!=None and request.POST.get('nu')!='' :
            inp=str(request.POST.get('nu'))
            if inp.isdigit(): 
                nu=int(request.POST.get('nu'))
            else:
                nu=float(request.POST.get('nu'))
        else:
            nu=0

        if given_data=="form1" and nu:
            di={"id":0,"sum":0,"l":[],"val":0,"nu":0, "given_data":given_data}
            nu = request.POST.get('nu')
            prob=0
            data=[]
            ans={}
            count=0
            for i in range(int(nu)):
                d=check_decimal_values(request.POST.get('r'+str(i)))
                p=check_decimal_values(request.POST.get('s'+str(i)))
                data.append(d*p)
                prob+=p
                ans["d{0}".format(i)] = d
                ans["p{0}".format(i)] = p
                di["d{0}".format(i)] = d
                di["p{0}".format(i)] = p
                count+=1
            di["nu"]=nu 
            di["id"]=1
            di["l"]=ans
            di["val"]=str(count)
            
            if prob==1:
                for i in range(len(data)):
                    di["m{0}".format(i)] = data[i]
                di["sum"]=round(sum(data),3)
                
            else:
                di["sum"]="Sum of Probability Distribution must be 1 "
                
            return render(request,'PROBABILITY/probability-distribution-calculator.html',dict(di))
        

        elif given_data=="form2" and nu:
            di={"id":0,"fin":0, "sum2":0, "sub":0, "sum":0,"sum1":0,"l":[],"l1":[],"val":0,"nu":0, "given_data":given_data}
            nu = request.POST.get('nu')
            prob=0
            data=[]
            data1 = []
            ans={}
            count=0
            for i in range(int(nu)):
                d=check_decimal_values(request.POST.get('r'+str(i)))
                p=check_decimal_values(request.POST.get('s'+str(i)))
                data.append(d*p)
                data1.append((d**2)*p)
                prob+=p
                ans["d{0}".format(i)] = d
                ans["p{0}".format(i)] = p
                di["d{0}".format(i)] = d
                di["p{0}".format(i)] = p
                count+=1
            di["nu"]=nu 
            di["id"]=1
            di["l"]=ans
            di["l1"] = ans
            di["val"]=str(count)
           
            if prob==1:
                for i in range(len(data)):
                    di["m{0}".format(i)] = data[i]
                di["sum2"]=round(sum(data),3)
                di["sum"]=round((sum(data)**2),3)

                for i in range(len(data1)):
                    di["m{0}".format(i)] = data1[i]
                di["sum1"]=round(sum(data1),3)

                di['sub'] = round(di["sum1"] - di["sum"] , 3)
                
                #fin = math.sqrt((round(sum(data1),3)) - (round((sum(data)**2),3)))
                di["fin"] = round(math.sqrt(di["sub"]) , 3)

                
            else:
                di["sum"]="Sum of Probability Distribution must be 1 "
                
            return render(request,'PROBABILITY/probability-distribution-calculator.html',dict(di))

        elif given_data=="form3" and nu:
            di={"id":0, "sum2":0, "sub":0, "sum":0,"sum1":0,"l":[],"l1":[],"val":0,"nu":0, "given_data":given_data}
            nu = request.POST.get('nu')
            prob=0
            data=[]
            data1 = []
            ans={}
            count=0
            for i in range(int(nu)):
                d=check_decimal_values(request.POST.get('r'+str(i)))
                p=check_decimal_values(request.POST.get('s'+str(i)))
                data.append(d*p)
                data1.append((d**2)*p)
                prob+=p
                ans["d{0}".format(i)] = d
                ans["p{0}".format(i)] = p
                di["d{0}".format(i)] = d
                di["p{0}".format(i)] = p
                count+=1
            di["nu"]=nu 
            di["id"]=1
            di["l"]=ans
            di["l1"] = ans
            di["val"]=str(count)
            
            if prob==1:
                for i in range(len(data)):
                    di["m{0}".format(i)] = data[i]
                di["sum2"]=round(sum(data),3)
                di["sum"]=round((sum(data)**2),3)

                for i in range(len(data1)):
                    di["m{0}".format(i)] = data1[i]
                di["sum1"]=round(sum(data1),3)

                di['sub'] = round(di["sum1"] - di["sum"] , 3)
                
                #fin = math.sqrt((round(sum(data1),3)) - (round((sum(data)**2),3)))
                
                
            else:
                di["sum"]="Sum of Probability Distribution must be 1 "
                
            return render(request,'PROBABILITY/probability-distribution-calculator.html',dict(di))

            
        else:
            di={ 'id':0, 'nu':0}
            return render(request,'PROBABILITY/probability-distribution-calculator.html',dict(di))
    else: 
        return render(request,'PROBABILITY/probability-distribution-calculator.html',{'given_data':'form1',"nu":0})


def probability_of_3_events_calculator(request):
    if request.method=="POST":
        a=float(request.POST['a'])
        b=float(request.POST['b'])
        c=float(request.POST['c'])
        if(a<0 or b<0 or c<0 or a>1 or b>1 or c>1):
            messages.info(request,"invalid value")
            return render(request, 'PROBABILITY/probability-of-3-events-calculator.html')
        else:
            description={}
            description['l1_bold']="Probability of all events occuring is P(A ∩ B ∩ C) = P(A) * P(B) * P(C)"
            description['l2_bold']="Probability of atleast one event occuring is P(A ∪ B ∪ C) = P(A) + P(B) + P(C) - P(A) * P(B) - P(A) * P(C) - P(B) * P(C) + P(A) * P(B) * P(C)"
            description['l3_bold']="Probability of exactly one event occuring is P(A ∩ B' ∩ C') + P(A' ∩ B ∩ C') + P(A' ∩ B' ∩ C) = P(A) * P(B') * P(C') + P(A') * P(B) * P(C') + P(A') * P(B') * P(C')"
            description['l4_bold']="Probability of none event occuring is P(∅) = 1 - (P(A) + P(B) + P(C) - P(A) * P(B) - P(A) * P(C) - P(B) * P(C) + P(A) * P(B) * P(C))"
            d=a*b*c
            e=a+b+c-(a*b)-(a*c)-(b*c)+(a*b*c)
            f=(1-a)*b*(1-c)+(1-b)*(1-c)*a+(1-a)*(1-b)*c
            g=1-e
            description['l4']="P(A ∩ B ∩ C) = "+str(d)
            description['l5']="P(A ∪ B ∪ C) = "+str(e)
            description['l6']="P(A ∩ B' ∩ C') + P(A' ∩ B ∩ C') + P(A' ∩ B' ∩ C) = "+str(f)
            description['l7']="P(∅) = "+str(g)
            return render(request, 'PROBABILITY/probability-of-3-events-calculator.html',context={"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g,"answer":description})
    return render(request, 'PROBABILITY/probability-of-3-events-calculator.html',{"a":0.5,"b":0.5,"c":0.5})

def random_number_generator(request):
  return render(request, 'PROBABILITY/random-number-generator.html')

def relative_risk_calculator(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        description={}
        if(int(a)<1 or int(b)<1 or int(c)<1 or int(d)<1):
            messages.info(request,"Invalid Value")
        else:
            description['l1_bold']="RR = [a / (a + b)] / [c / (c + d)]"
            description['l2']="where a is the number of members of the exposed group who developed the disease;"
            description['l3']="b is the number of members of the exposed group who didn't develop the disease;"
            description['l4']="c is the number of members of the control group who developed the disease;"
            description['l5']="d is the number of members of the control group who didn't develop the disease;"
            description['l6'] ="RR is the relative risk."
            e=(int(a)/((int(a)+int(b)))/(int(c)/((int(c)+int(d)))))
            description['l7']="Relative Risk = "+str(e)
            return render(request, 'PROBABILITY/relative-risk-calculator.html',context={'a':a,'b':b,"c":c,"d":d,"e":e,"answer":description})
    return render(request, 'PROBABILITY/relative-risk-calculator.html',{'a':1,'b':2,"c":3,"d":4})
def random_number_generator(request):
    try:
        ul = str(request.POST.get('ul'))
        ll = str(request.POST.get('ll'))
    

        if request.method == "POST":
            ul = int(request.POST.get('ul'))
            ll = int(request.POST.get('ll'))
            re = random.randint(ll,ul)
            context = {
                'ul':ul,
                'll':ll,
                'result':re,
                'ot':True
            }
            return render(request,'PROBABILITY/random-number-generator.html',context)
        return render(request,'PROBABILITY/random-number-generator.html',{'ll':1,'ul':50,'ot':False})
    except:
        messages.error(request,'Please Enter valid data')
        return render(request,'PROBABILITY/random-number-generator.html',{'ll':1,'ul':50,'ot':False})

def risk_calculator(request):
    
    
    if request.method == "POST":
        user_input = check_decimal_values(request.POST.get('probability'))
        user_input2 = check_decimal_values(request.POST.get('loss'))

        risk = round((user_input*user_input2),4)
        d={'risk':risk,'probability':user_input,'loss':user_input2,'id':1}
        return render(request, "PROBABILITY/risk-calculator.html",d)
        
    else:
        d={'risk':10,'probability':5,'loss':2}
        return render(request, "PROBABILITY/risk-calculator.html",d)  


def roulette_probability_calculator(request):
    errors = []
    if request.method=='POST':
        try:
            type = request.POST.get('type')
            amount = float(request.POST.get('amount'))
            betting = request.POST.get('betting')
        except:
            errors.append(
                "Unable to get necessary input, please try again."
            )
        gamerule1 = ["Red" , "Black" , "Odds" , "Evens"]
        gamerule2 = ["1-12" , "13-24" ,"25-36"]
        if type == "European":
            if betting in gamerule1:
                outcomeprobability = 18/37
                successpercentage = outcomeprobability*100
                yourwin = 2*amount
            elif betting in gamerule2:
                outcomeprobability = 12/37
                successpercentage = outcomeprobability*100
                yourwin = 3*amount
            elif betting == "Straight":
                outcomeprobability = 1/37
                successpercentage = outcomeprobability*100
                yourwin = 36*amount
            elif betting == "Split":
                outcomeprobability = 2/37
                successpercentage = outcomeprobability*100
                yourwin = 18*amount
            elif betting == "Street":
                outcomeprobability = 3/37
                successpercentage = outcomeprobability*100
                yourwin = 12*amount
            elif betting == "Square":
                outcomeprobability = 4/37
                successpercentage = outcomeprobability*100
                yourwin = 9*amount
            elif betting == "Sixline":
                outcomeprobability = 6/37
                successpercentage = outcomeprobability*100
                yourwin = 6*amount
                

            
            context = {
                'id':1,
                'errors':errors,
                'amount':amount,
                'betting':betting,
                'outcomeprobability':outcomeprobability,
                'successpercentage':successpercentage,
                'yourwin':yourwin,
                
            }
            return render(request,'PROBABILITY/roulette-probability-calculator.html',context)
        else:
            if betting in gamerule1:
                outcomeprobability = 18/38
                successpercentage = outcomeprobability*100
                yourwin = 2*amount
            elif betting in gamerule2:
                outcomeprobability = 12/38
                successpercentage = outcomeprobability*100
                yourwin = 3*amount
            elif betting == "Straight":
                outcomeprobability = 1/38
                successpercentage = outcomeprobability*100
                yourwin = 36*amount
            elif betting == "Split":
                outcomeprobability = 2/38
                successpercentage = outcomeprobability*100
                yourwin = 18*amount
            elif betting == "Street":
                outcomeprobability = 3/38
                successpercentage = outcomeprobability*100
                yourwin = 12*amount
            elif betting == "Square":
                outcomeprobability = 4/38
                successpercentage = outcomeprobability*100
                yourwin = 9*amount
            elif betting == "Sixline":
                outcomeprobability = 6/38
                successpercentage = outcomeprobability*100
                yourwin = 6*amount
                

            
            context = {
                'id':1,
                'errors':errors,
                'amount':amount,
                'betting':betting,
                'outcomeprobability':outcomeprobability,
                'successpercentage':successpercentage,
                'yourwin':yourwin,
                
            }
            return render(request,'PROBABILITY/roulette-probability-calculator.html',context)



    return render(request,'PROBABILITY/roulette-probability-calculator.html',{"amount":1000})


def standard_deviation_probability_calculator(request):
    if request.method == "POST":
            num1=request.POST.get("n")
            x1=num1.split(',')
            x2=[]
            for i in x1:
                try:
                    x2.append(int(i))
                except:
                    x2.append(float(i))
            mn=0
            for i in x2:
                mn+=i
            mn_res=mn/len(x2)
            sum_squares=0
            for i in x2:
                b1=(i-mn_res)**2
                sum_squares+=b1
            import statistics
            res=statistics.stdev(x2)
            result=round(res**2,5)
            return render(request, 'PROBABILITY/standard-deviation-probability-calculator.html',{"n":num1,"result":result})
    else:
        return render(request, 'PROBABILITY/standard-deviation-probability-calculator.html',{"n":"18,23,56,34,23"})



def uniform_probability_distribution_calculator(request):
    if request.method == "POST":
        f = request.POST.get('number_of_times_event_occurs')
        n = request.POST.get('number_of_times_experiment_performed')
        empirical_probab = round(int(f) / int(n),4)

        context = {
            'number_of_times_event_occurs':f,
            'number_of_times_experiment_performed':n,
            'empirical_probab': empirical_probab,
            'id':1
        }
        return render(request, "PROBABILITY/uniform-probability-distribution-calculator.html", context)
    else:
        d = {'number_of_times_event_occurs':4,'number_of_times_experiment_performed':2}
        return render(request, "PROBABILITY/uniform-probability-distribution-calculator.html",d)



def variance_calculator_probability(request):
    if request.method=='POST':
        num1=request.POST.get("input1")
        try:
            x1=num1.split(',')
            x2=[]
            for i in x1:
                try:
                    x2.append(int(i))
                except:
                    x2.append(float(i))
            mn=0
            for i in x2:
                mn+=i
            mn_res=mn/len(x2)
            sum_squares=0
            for i in x2:
                b1=(i-mn_res)**2
                sum_squares+=b1
            import statistics
            res=statistics.stdev(x2)
            result=round(res**2,5)
            v=[]
            a=v.append
            a('<p><strong>Standard Deviation:</strong></p>')
            a('<p>{}</p>'.format(res))
            a('<p><strong>Sum of Squares:</strong></p>')
            a('<p>{}</p>'.format(sum_squares))
            a('<p><strong>Variance:</strong></p>')
            a('<p>{}</p>'.format(result))
            a('<p><strong>Mean:</strong></p>')
            a('<p>{}</p>'.format(mn_res))
            a('<p><strong>Count:</strong></p>')
            a('<p>{}</p>'.format(len(x2)))
            context={'input1':num1,'detailStep':''.join(v),'go_tag':'#variance'}
            return render(request,'PROBABILITY/variance-calculator-probability.html',context)
        except:
            messages.error(request,"Enter a valid input")
            context={'input1':num1}
            return render(request,'PROBABILITY/variance-calculator-probability.html',context)
    else:
	    return render(request,'PROBABILITY/variance-calculator-probability.html')

def yugioh_probability_calculator(request):
  return render(request, 'PROBABILITY/yugioh-probability-calculator.html')



def z_score_probability_calculator(request):
    if request.method=='POST':
        num1=request.POST.get("input1")
        num2=request.POST.get("input2")
        num3=request.POST.get("input3")
        try:
            try:
                n1=int(num1)
            except:
                n1=float(num1)
            try:
                n2=int(num2)
            except:
                n2=float(num2)
            try:
                n3=int(num3)
            except:
                n3=float(num3)
            r1=n1-n2
            r2=r1/n3
            v=[]
            a=v.append
            a('<p><strong>Z-score:</strong></p>')
            a('<p>{}</p>'.format(r2))
            return render(request,'PROBABILITY/z-score-probability-calculator.html',{'input1':num1,'input2':num2,'input3':num3,'detailStep':''.join(v),'go_tag':'#z_score'})
        except:
            messages.error(request,"Enter a valid input")
            return render(request,'PROBABILITY/z-score-probability-calculator.html',{'input1':num1,'input2':num2,'input3':num3})
    else:
	    return render(request,'PROBABILITY/z-score-probability-calculator.html')



def marbleprob(request):
    if request.method == "POST":
        di={}
        nu = request.POST.get('nu')
        for i in range(int(nu)):
            d=request.POST.get('r'+str(i))
            p=check_decimal_values(request.POST.get('s'+str(i)))
            di[d]=p
        s=request.POST.get("s")
        if s==None:
            
            messages.error(request, "Please select one option")
            return render(request,"PROBABILITY/bag-of-marble-pobability.html")
        else:
            opt=[]
            total=0
            fav=0
            for i in di.items():
                if i[0] in s:
                    fav+=i[1]
                total+=i[1]
            prob=fav/total
            context={
                "fav":fav,
                "total":total,
                "prob":prob,
                "di":di,
                "con":s,
                "id":1,
                "nu":0
                            
                }
           
            
            return render(request,"PROBABILITY/bag-of-marble-pobability.html",context)
    else:
        return render(request,"PROBABILITY/bag-of-marble-pobability.html",{"nu":0})