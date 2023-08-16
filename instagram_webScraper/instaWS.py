#!/usr/bin/env python
# coding: utf-8

# In[80]:


#essensial to install instagram-scraper package!
import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import threading 
import time
import os
import json
import pandas as pd
from tkinter import *


# In[99]:


start = time.perf_counter()


# In[101]:


os.system('pip install instagram-scraper')


# In[45]:


'''<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Main>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
hashtag = input('Eter the HASHTAG : ')
n= int(input('Enter n(number of pages): '))
m= int(input('Enter m(number of pages): '))

username=input('Enter your USERNAME: ')
password=input('Enter your PASSWORD: ')
print('Wait a few minutes...')
COMMAND='instagram-scraper --media-metadata -u {} -p {} {} --media-types none --comments  --maximum {}'


# In[47]:



browser = webdriver.Edge("D:\IUST works\python\instagram scrapper\mine\msedgedriver.exe")
browser.maximize_window()

browser.get('https://www.instagram.com/')
time.sleep(5)


# In[48]:


xpath='//*[@id="loginForm"]/div/div[1]/div/label/input'
username_sec= browser.find_element_by_xpath(xpath)
username_sec.send_keys(username)
time.sleep(0.5)


# In[49]:


xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
password_sec = browser.find_element_by_xpath(xpath)
password_sec.send_keys(password)
time.sleep(0.5)


# In[50]:


xpath='//*[@id="loginForm"]/div/div[3]/button'
login_btn = browser.find_element_by_xpath(xpath)
login_btn.click()
time.sleep(5)


# In[51]:


xpath='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
search_box=browser.find_element_by_xpath(xpath)
search_box.send_keys('#'+hashtag)
time.sleep(10)


# In[52]:


xpath='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div'
first =browser.find_element_by_xpath(xpath)
first.click()
time.sleep(4)


# In[53]:


posts=browser.find_elements_by_class_name('_9AhH0')


# In[56]:


ids_list=[]
# get IDs:
for post in posts[0:m]:
    post.click()
    time.sleep(4)
    user_id= browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')
    x=user_id.text
    ids_list.append(x)
    x_btn=post.find_element_by_xpath('/html/body/div[5]/div[1]/button')
    x_btn.click()


# In[57]:


def make_json(i):
    os.system(COMMAND.format(username , password , ids_list[i] , m))


# In[58]:


threads=[]
for i in range (n):
    t = threading.Thread(target=make_json , args=[i])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()


# In[ ]:





# In[ ]:





# In[67]:


df = pd.DataFrame(columns=['User','LikesNumber', 'URL','UserWhoComment','comment'],)


# In[68]:


threads=[]


# In[69]:


def get_info(name ): 
 
    # name = 'lagambetasports'  
    with open('.\{}\{}.json'.format(name,name) , encoding="utf8") as f:
        data = json.loads(f.read())
    #     print(data['GraphImages'][0])
    secs=[]
    for i in range(m):
        like_num = data['GraphImages'][i]['edge_media_preview_like']['count']
        url=data['GraphImages'][i]['display_url']
        
        user=data['GraphImages'][i]['username']
        for j in range (int(data['GraphImages'][i]['edge_media_to_comment']['count'])):
            new_row = {'User':user,'LikesNumber': like_num,'URL': url,'UserWhoComments': data['GraphImages'][i]['comments']['data'][j]['owner']['username'] , 'comment': data['GraphImages'][i]['comments']['data'][j]['text']}    
            # df.iloc[1] = [user, like_num, url, data['GraphImages'][i]['comments']['data'][j]['owner']['username'] ,  data['GraphImages'][i]['comments']['data'][j]['text'] ]  
            # ['User','LikesNumber', 'URL','UserWhoComments','comment']
            secs.append(new_row)
            # d = d.append(*secs , ignore_index=True)
            s = pd.Series([user , like_num , url , data['GraphImages'][i]['comments']['data'][j]['owner']['username'] ,data['GraphImages'][i]['comments']['data'][j]['text'] ],index=['User','LikesNumber', 'URL','UserWhoComments','comment'])
            df.loc[len(df)] =[user, like_num, url, data['GraphImages'][i]['comments']['data'][j]['owner']['username'] ,  data['GraphImages'][i]['comments']['data'][j]['text'] ] 

    #  df = df.append(s,ignore_index=True)
    # for i in range(m):
    #     d = d.append(secs , ignore_index=True)
    #     print(*secs,end='\n')


# In[ ]:





# In[72]:



for id in ids_list:
    t = threading.Thread(target=get_info , args=[id])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()


# In[20]:


df.to_excel('RESULTS.xlsx')


# In[75]:


end= time.perf_counter()


# In[76]:


taken_time = end - start


# In[97]:



class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='USERNAME:')
        self.lbl2=Label(win, text='PASSWORD:')
        self.lbl3=Label(win, text='m(for posts):')
        self.lbl4=Label(win, text='n(for pages):')
        self.lbl5=Label(win, text='HASHTAG:')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.btn6 = Button(win, text='GO!')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=200, y=250)
        self.b1=Button(win, text='GO!', command=self.go) 
        self.b1.place(x=150, y=300)
        self.tn=Entry()
        self.tn.place(x=150, y=400)
    def go(self):
        num_n=int(self.t3.get())
        num_m=int(self.t4.get())
        h=self.t5.get()
        u=self.t1.get()
        p=self.t2.get()
        result=scrap(u,p,n,m,h)
        self.t3.insert(END, str(result))
        


# In[98]:


window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x600+10+10")
window.mainloop()


# In[ ]:




