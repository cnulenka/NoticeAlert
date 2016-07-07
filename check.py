import urllib2
import re
import extract
import logging


def checkupdates():
        logging.info("Reading from file")
        f=open('docid.txt')
        lists=[]
        lists=map(int,f)
        docid=lists[0]
        f.close()
        logging.info("Reading complete.")
        logging.info("Starting to check for update")
        url= 'http://hib.iiit-bh.ac.in/Hibiscus/Pub/nbDocDet.php?docid={}&client=iiit&iframe=true&nb=Y'.format(docid)
        logging.info("Trying to fetch d url")
        resp = urllib2.urlopen(url)
        respData = resp.read()
        logging.info("Fetching complete.")
        regex='<h1 style="BACKGROUND-COLOR: white; line-height: 2em; margin:0 .5em .2em .5em; padding: 4px 8px 4px 8px; border-radius: 10px;-moz-border-radius: 10px; -webkit-border-radius: 10px; border: 1px solid silver;text-decoration:none; font-size: 2.1em;">(.*?)</h1>'
        pattern =re.compile(regex)
        header=re.findall(pattern,respData)
        logging.info("Got the header")
        if not header:
            logging.info("No new notice found")
            pass
        else:
            logging.info("Got a new notice")
            logging.info("Writing to file")
            docid=docid+1
            f=open('docid.txt','w')
            f.write(str(docid))
            f.close()
            logging.info("Writing  complete.")
            try:
                logging.info("sending html to extract")
                extract.extract(respData,header[0],url)
            except Exception as e:
                logging.error("Calling extract failed %s",e)      
    
if __name__ == "__main__":
    log_level = logging.DEBUG
    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s()\t%(message)s"
    logging.basicConfig(format=log_format, level=log_level) 
