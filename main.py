#!/usr/bin/env python

from check import checkupdates
import os
from time import sleep
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib2
import re

        
def my_job():
  log_level = logging.DEBUG
  log_format = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s()\t%(message)s"
  logging.basicConfig(filename='logfile.log',format=log_format, level=log_level) 
  checkupdates()  
 
if __name__ == '__main__':
    url="http://hib.iiit-bh.ac.in/Hibiscus/Pub/nbDocList.php?client=iiit"
    resp=urllib2.urlopen(url)
    respdata=resp.read()
    regex="docid=(.*?)&client=iiit"
    pattern =re.compile(regex)
    number=re.findall(pattern,respdata)
    lists=[]
    lists=map(int,number)
    docid=lists[0]+1
    while(True):
        url= 'http://hib.iiit-bh.ac.in/Hibiscus/Pub/nbDocDet.php?docid={}&client=iiit&iframe=true&nb=Y'.format(docid)
        resp = urllib2.urlopen(url)
        respData = resp.read()
        regex='<h1 style="BACKGROUND-COLOR: white; line-height: 2em; margin:0 .5em .2em .5em; padding: 4px 8px 4px 8px; border-radius: 10px;-moz-border-radius: 10px; -webkit-border-radius: 10px; border: 1px solid silver;text-decoration:none; font-size: 2.1em;">(.*?)</h1>'
        pattern =re.compile(regex)
        header=re.findall(pattern,respData)
        if not header:
            break   
        else:
            docid=docid+1
    f=open('docid.txt','w')
    f.write(str(docid))
    f.close()
    sched = BlockingScheduler()
    sched.add_job(my_job, 'interval', minutes=2)
    try:
            sched.start()
    except (KeyboardInterrupt, SystemExit):
             pass
