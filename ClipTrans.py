#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyperclip
import time
from selenium import webdriver
import urllib.parse
import re


# In[2]:


def ChangeTxt(text):
    text=(
        text
        .replace("\r","")
        .replace(" -\n","")
        .replace("-\n","")
        .replace("\n"," ")
        .replace("|","｜")
        .replace(" ̃","")
        .replace("/","／")
        .replace("] .","].")
    )
    text=re.sub(r"\[[0-9\, ]*\]","",text) #引用
    text=(
        text
        .replace("   "," ")
        .replace("  "," ")
        .replace("w.r.t. ","w.r.t.")
        .replace("et. al","et.al")
        .replace("i.e. ","i.e.")
        .replace(". ",".\n\n")
        .replace("; ",";\n\n")
        .replace("𝑘","k")
        .replace("𝑘","k")
        .replace("𝑙","l")
        .replace("𝑢","u")
        .replace("𝑧","z")
        .replace("𝐾","K")
        .replace("","fi")
        .replace("","th")
    )
    return text


# In[3]:


cliptext=""
browser = webdriver.Firefox()
while True:
    time.sleep(0.2)
    tmp=pyperclip.paste()
    if tmp!=cliptext:
        cliptext=tmp
        text=ChangeTxt(cliptext)
        text=urllib.parse.quote(text)
        browser.get(r"https://www.deepl.com/ja/translator#en/ja/"+text)

