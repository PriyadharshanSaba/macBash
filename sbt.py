#!/usr/bin/env python

#PD_SubsRETR : Fetch Movies Subtitles with One click!
#Creator / Developer Name : Priyadharshan Saba
#Script : Shell Script, Python, Apple Scripts
#Python Dependencis: mechanize :   https://pypi.python.org/pypi/mechanize/
#                    BeautifulSoup4 : https://pypi.python.org/pypi/beautifulsoup4
#Runtime : Python 2
#OS Requirements: Mac OSX , macOS

import imp
import sys
import os
def name():
    i=0
    mname=""
    nam=""
    row_count=0
    for x in sys.argv:
        x=x.split(" ")
        for i in x:
            if row_count>=1:
                mname=mname+str(i)+" "
            row_count+=1
        mname=nam+mname
    mname=mname.strip()
    return mname

def openBots(name):
    try:
        sys.path.append("/usr/local/lib/python2.7/site-packages")
        import mechanize
        from bs4 import BeautifulSoup
    except:
        sys.exit()
    name=name.strip().lower()
    name=name.split('.')
    name=name[0]
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        op=br.open("http://www.yifysubtitles.com")
        br.select_form(nr=0)
        br.form['q']=name
        sub = br.submit()
        soup = BeautifulSoup(sub.read(),"lxml")
        row_count=0
        for div in soup.findAll('div',{'class':'col-sm-12'}):
            row_count+=1
            if row_count==1:
                dd=div.find('div',{'class':'media-body'})
                di=dd.find('a')
                fnam = di.text.strip().lower().split("\n")
                link=di['href']
            elif row_count>1:
                break

        op=br.open(link)
        soup = BeautifulSoup(op.read(),"lxml")
        row_count=0
        for table in soup.findAll('table',{'class':'table other-subs'}):
            for td in table.findAll('td',{'class':'flag-cell'}):
                row_count+=1
                if td.text.lower().strip() == "english":
                    break

        for table in soup.findAll('table',{'class':'table other-subs'}):
            rc=0
            row_count= (row_count*3) - 3
            for a in table.findAll('a'):
                if rc==row_count:
                    link1 = a['href']
                    break
                else:
                    rc+=1

        op=br.open(link1)
        soup = BeautifulSoup(op.read(),"lxml")

        row_count=0
        for div in soup.findAll('div',{'class':'col-xs-12'}):
            if row_count==2:
                x= div.text.split('\n')
                fnam = x[1].strip()+".srt"
            row_count+=1
        for a in soup.findAll('a',{'class':'btn-icon download-subtitle'}):
            down_link= a['href']
        br.retrieve(down_link,fnam)
    except:
        sys.exit()

mname=name()
openBots(mname)

