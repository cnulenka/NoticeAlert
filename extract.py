import re
import finaltext
import logging
import HTMLParser

def extract(html,header,url):
        logging.info("inside the extract function")
        regex2="Posted By: (.*?)\|"
        regex3="Attention: (.*?) \|"
        pattern2=re.compile(regex2)
        pattern3=re.compile(regex3)
        posted=re.findall(pattern2,html)
        attention=re.findall(pattern3,html)
        html_parser = HTMLParser.HTMLParser()
        header = html_parser.unescape(header)
        posted = html_parser.unescape(posted[0])
        attention = html_parser.unescape(attention[0])
        logging.info("Extraction complete")
        try:
            finaltext.finaltext(header,posted,attention,url)
        except Exception as e:
            logging.error("Calling finaltext failed %s",e)
    
if __name__ == "__main__":
    log_level = logging.DEBUG
    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s()\t%(message)s"
    logging.basicConfig(format=log_format, level=log_level) 
