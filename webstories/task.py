import os
import json
import requests
from bs4 import BeautifulSoup
import shutil

def download(src,path):
    r = requests.get(src, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media/web-stories')
output=[]
def best_web_stories_scrapper():
    best=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),r'webstories/utils')
    file1 = open(os.path.join(best,'best.txt'),"r")
    links=(file1.readlines()) 
    for i in range(len(links)):
        links[i]=links[i].replace("\n","")
    # print(len(links),type(links[0]))
    
    for i in range(len(links)):
        d={}
        Web_url = links[i]
        r = requests.get(Web_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        meta=soup.findAll('meta',{'property':['og:description','og:title','og:url']})
        try:
            d['content']=meta[0].get('content').replace("USA","NEWS").replace("10Best","")
        except:
            d['content']=''
        try:
            d['title']=meta[1].get('content').replace("USA","NEWS").replace("10Best","")
        except:
            d['title']=''

        
       
        try:
            url=meta[2].get('content')
            url=list(url.split('/'))
            d['url']=url[-2]
            
            if d not in output:
                output.append(d)
        except:
            d['url']=''
        # print(d)
        
    json_dump=json.dumps(output)

    # file_name=os.path.join(path,"title-description-best.json")

    # with open(file_name, "w") as outfile:
    #     outfile.write(json_dump)
    for i in range(len(links)):
        Web_url = links[i]
    
        r = requests.get(Web_url)
        webstoryno=Web_url.split("/")[-2]
        print(webstoryno)
        
        dir_path=os.path.join(path,"webstory-"+str(webstoryno))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            soup = BeautifulSoup(r.content, 'html.parser')
                #code added for posters
            standAlone = soup.find('amp-story')

            if standAlone.get('poster-portrait-src') != None:
                portrait = standAlone.get('poster-portrait-src')
                if portrait != None:
                    src="webstory-"+str(webstoryno)+"-portrait.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(portrait,src)
                    except:
                        print(portrait,src,webstoryno) 

            if standAlone.get('poster-landscape-src') != None:
                landscape = standAlone.get('poster-landscape-src')
                if landscape != None:
                    src="webstory-"+str(webstoryno)+"-landscape.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(landscape,src)
                    except:
                        print(landscape,src,webstoryno)

            if standAlone.get('poster-square-src') != None:            
                square = standAlone.get('poster-square-src')
                if square != None:
                    src="webstory-"+str(webstoryno)+"-square.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(square,src)
                    except:
                        print(square,src,webstoryno)
                #code ends here for poster

            stories=soup.findAll('amp-story-page')
            output1=[]
            items=0
            for st in stories:
                story={}
                story['url']=Web_url.split('/')[-2]
                headings=(st.findAll('h1'))
                subheadings=(st.findAll('h2'))
                paras=(st.findAll('p'))
                story['heading']=[]
                for heading in headings:
                    story['heading'].append(heading.text.replace("USA","NEWS").replace("10Best",""))
                story['subheading']=[]
                for subheading in subheadings:
                    story['subheading'].append(subheading.text.replace("USA","NEWS").replace("10Best",""))
                story['para']=[]
                for para in paras:
                    story['para'].append(para.text.replace("USA","NEWS").replace("10Best",""))
                image=st.find('amp-img')
                poster=st.find('amp-video')
                video=st.findAll('source')
                story['image']=""
                story['poster']=""
                story['video']=""
                if image:
                    items+=1
                    src=image['src']
                    img_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['image']=src
                    src=os.path.join(dir_path,src)
                    print(img_src,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get(img_src).content)
                        f.close()
                    except:
                        print(img_src,src,webstoryno)
                if poster:
                    items+=1
                    src=poster['poster']
                    post_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['poster']=src
                    src=os.path.join(dir_path,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get(post_src).content)
                        f.close()
                    except:
                        print(post_src,src,webstoryno)
                if video:
                    items+=1
                    src=video[-1]['src']
                    video_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['video']=src
                    src=os.path.join(dir_path,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get(video_src).content)
                        f.close()
                    except:
                        print(video_src,src,webstoryno)
                output1.append(story)
            # print("No of items:",items+1)
            json_dump=json.dumps(output1)
            file_name=os.path.join(path,"webstory-"+str(webstoryno))
            file_name=os.path.join(file_name,"webstory-"+str(webstoryno)+".json")
            with open(file_name, "w") as outfile:
                outfile.write(json_dump)
    best=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),r'webstories/utils')

    file1 = open(os.path.join(best,'USA_Today Web Stories.txt'),"r")
    links=(file1.readlines()) 
    for i in range(len(links)):
        links[i]=links[i].replace("\n","")
    # print(len(links),type(links[0]))
    
    for i in range(len(links)):
        d={}
        Web_url = links[i]
        r = requests.get(Web_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        meta=soup.findAll('meta',{'property':['og:description','og:title','og:url']})
        try:
            d['content']=meta[0].get('content').replace("USA","NEWS")
        except:
            d['content']=''
        try:
            d['title']=meta[1].get('content').replace("USA","NEWS")
        except:
            d['title']=''
        
       
        try:
            url=meta[2].get('content')
            url=list(url.split('/'))
            d['url']=url[-2]
            if d not in output:
                output.append(d)
        except:
            d['url']=''
        # print(d)
        
    json_dump=json.dumps(output)

    # file_name=os.path.join(path,"title-description-usa.json")

    # with open(file_name, "w") as outfile:
    #     outfile.write(json_dump)
    for i in range(len(links)):
        Web_url = links[i]
    
        r = requests.get(Web_url)
        webstoryno=Web_url.split("/")[-2]
        print(webstoryno)
        
        dir_path=os.path.join(path,"webstory-"+str(webstoryno))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            soup = BeautifulSoup(r.content, 'html.parser')

            #code added for posters
            standAlone = soup.find('amp-story')
            address = Web_url.split('/')[-2]
            if standAlone.get('poster-portrait-src') != None:
                portrait = standAlone.get('poster-portrait-src')
                if portrait != None:
                    src="webstory-"+str(webstoryno)+"-portrait.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download("https://www.usatoday.com/web-stories/"+"/"+address+"/"+portrait,src)
                    except:
                        print(portrait,src,webstoryno) 

            if standAlone.get('poster-landscape-src') != None:
                landscape = standAlone.get('poster-landscape-src')
                if landscape != None:
                    src="webstory-"+str(webstoryno)+"-landscape.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download("https://www.usatoday.com/web-stories/"+"/"+address+"/"+landscape,src)
                    except:
                        print(landscape,src,webstoryno)

            if standAlone.get('poster-square-src') != None:            
                square = standAlone.get('poster-square-src')
                if square != None:
                    src="webstory-"+str(webstoryno)+"-square.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download("https://www.usatoday.com/web-stories/"+"/"+address+"/"+square,src)
                    except:
                        print(square,src,webstoryno)
                #code ends here for poster

            stories=soup.findAll('amp-story-page')
            output1=[]
            items=0
            for st in stories:
                story={}
                story['url']=Web_url.split('/')[-2]
                headings=(st.findAll('h1'))
                subheadings=(st.findAll('h2'))
                paras=(st.findAll('p'))
                story['heading']=[]
                for heading in headings:
                    story['heading'].append(heading.text.replace("USA","NEWS"))
                story['subheading']=[]
                for subheading in subheadings:
                    story['subheading'].append(subheading.text.replace("USA","NEWS"))
                story['para']=[]
                for para in paras:
                    story['para'].append(para.text.replace("USA","NEWS"))
                image=st.find('amp-img')
                poster=st.find('amp-video')
                video=st.findAll('source')
                story['image']=""
                story['poster']=""
                story['video']=""
                if image:
                    items+=1
                    src=image['src']
                    img_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['image']=src
                    src=os.path.join(dir_path,src)
                    print(img_src,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get("https://www.usatoday.com/web-stories/"+"/"+story['url']+"/"+img_src).content)
                        f.close()
                    except:
                        print(img_src,src,webstoryno)
                if poster:
                    items+=1
                    src=poster['poster']
                    post_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['poster']=src
                    src=os.path.join(dir_path,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get("https://www.usatoday.com/web-stories/"+"/"+story['url']+"/"+post_src).content)
                        f.close()
                    except:
                        print(post_src,src,webstoryno)
                if video:
                    items+=1
                    src=video[-1]['src']
                    video_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['video']=src
                    src=os.path.join(dir_path,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get("https://www.usatoday.com/web-stories/"+"/"+story['url']+"/"+video_src).content)
                        f.close()
                    except:
                        print(video_src,src,webstoryno)
                output1.append(story)
            # print("No of items:",items+1)
            json_dump=json.dumps(output1)
            file_name=os.path.join(path,"webstory-"+str(webstoryno))
            file_name=os.path.join(file_name,"webstory-"+str(webstoryno)+".json")
            with open(file_name, "w") as outfile:
                outfile.write(json_dump)
    best=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),r'webstories/utils')

    file1 = open(os.path.join(best,'popsugr.txt'),"r")
    
    links=(file1.readlines()) 
    for i in range(len(links)):
        links[i]=links[i].replace("\n","")
    print(len(links),type(links[0]))


    
    for i in range(len(links)):
        d={}
        Web_url = links[i]
        r = requests.get(Web_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        try:
            meta=soup.findAll('meta',{'property':['og:url','og:title','keywords']})
            print(meta)
            for m in meta:
                print(m['property'])
                if m['property'] == "og:title":
                    title = m.get('content')
                    
                if m['property'] == "keywords":
                    cont = m.get('content')
                    
                if m['property'] == "og:url":
                    url = m.get('content')
                    url=list(url.split('/'))
                    ul=url[-2]
                    
            d['content'] = cont.replace("POPSUGR","") if cont else ""
            d['title'] = title.replace("POPSUGR","") if title else ""
            d['url'] = ul
            
            if d not in output:
                output.append(d)
            
        except:
            d['url']=''
    
    print(output)
    json_dump=json.dumps(output)
    file_name=os.path.join(path,"title-description.json")
    with open(file_name, "w") as outfile:
        outfile.write(json_dump)


    for i in range(len(links)):
        Web_url = links[i]
        print(Web_url)
        r = requests.get(Web_url)
        webstoryno=Web_url.split("/")[-2]
        
        dir_path=os.path.join(path,"webstory-"+str(webstoryno))
        output1=[]
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            soup = BeautifulSoup(r.content, 'html.parser')

            #code added for posters
            standAlone = soup.find('amp-story')
            address = Web_url.split('/')[-2]
            if standAlone.get('poster-portrait-src') != None:
                portrait = standAlone.get('poster-portrait-src')
                if portrait != None:
                    src="webstory-"+str(webstoryno)+"-portrait.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(f"https://www.popsugar.com/stories/{address}/{portrait}",src)
                    except:
                        print(portrait,src,webstoryno) 

            if standAlone.get('poster-landscape-src') != None:
                landscape = standAlone.get('poster-landscape-src')
                if landscape != None:
                    src="webstory-"+str(webstoryno)+"-landscape.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(f"https://www.popsugar.com/stories/{address}/{landscape}",src)
                    except:
                        print(landscape,src,webstoryno)

            if standAlone.get('poster-square-src') != None:            
                square = standAlone.get('poster-square-src')
                if square != None:
                    src="webstory-"+str(webstoryno)+"-square.jpg"
                    src=os.path.join(dir_path,src)
                    try:
                        download(f"https://www.popsugar.com/stories/{address}/{square}",src)
                    except:
                        print(square,src,webstoryno)
                #code ends here for poster

            stories=soup.findAll('amp-story-page')
          
            items=0
            for st in stories:
                story={}
                story['url']=Web_url.split('/')[-2]
                headings=(st.findAll('h1'))
                # subheadings=(st.findAll('h2'))
                paras=(st.findAll('p'))
                story['heading']=[]
                story['subheading']=[]
                story['para']=[]
                if len(headings) == 1:
                    if paras:
                        story['para'].append(paras[0].text)
                        story['subheading'].append(headings[0].text.replace("POPSUGR",""))
                    else:       
                        story['para'].append(headings[0].text.replace("POPSUGR",""))
                elif len(headings) == 2:
                    if paras:
                        story['para'].append(paras[0].text.replace("POPSUGR",""))
                        story['subheading'].append(headings[0].text.replace("POPSUGR",""))
                        story['heading'].append(headings[1].text.replace("POPSUGR",""))
                    else:
                        story['subheading'].append(headings[1].text.replace("POPSUGR",""))
                        story['para'].append(headings[0].text.replace("POPSUGR",""))
                elif len(headings) == 3:
                    if paras:
                        story['para'].append(paras[0].text.replace("POPSUGR",""))
                        story['subheading'].append(headings[0].text.replace("POPSUGR",""))
                        story['subheading'].append(headings[1].text.replace("POPSUGR",""))
                        story['heading'].append(headings[2].text.replace("POPSUGR",""))
                    else:
                        story['heading'].append(headings[2].text.replace("POPSUGR",""))
                        story['subheading'].append(headings[1].text.replace("POPSUGR",""))
                        story['para'].append(headings[0].text.replace("POPSUGR",""))
                

                

                image=st.find('amp-story-grid-layer')
                image=image.find('amp-img')
                # poster=st.find('amp-video')
                video=st.findAll('source')
                
                story['image']=""
                story['poster']=""
                story['video']=""
                if image:
                    items+=1
                    # src=image['src']
                    src = f"https://www.popsugar.com/stories/{story['url']}/{image['src']}"
                    img_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['image']=src
                    
                    src=os.path.join(dir_path,src)
                    try:
                        f = open(src,'wb')
                        f.write(requests.get(img_src).content)
                        f.close()
                    except:
                        print(img_src,src,webstoryno)
            
                if video:
                    items+=1
                    # src=video[-1]['src']
                    src = f"https://www.popsugar.com/stories/{story['url']}/{video[-1]['src']}"
                    video_src=src
                    src=list(src.split('/'))
                    src="webstory-"+str(webstoryno)+"-"+src[-1]
                    story['video']=src
                    
                    src=os.path.join(dir_path,src)
                    
                    try:
                        f = open(src,'wb')
                        f.write(requests.get(video_src).content)
                        f.close()
                    except:
                        print(video_src,src,webstoryno)
                output1.append(story)
            print("No of items:",items+1)
            json_dump=json.dumps(output1)
            file_name=os.path.join(path,"webstory-"+str(webstoryno))
            file_name=os.path.join(file_name,"webstory-"+str(webstoryno)+".json")
            with open(file_name, "w") as outfile:
                outfile.write(json_dump)