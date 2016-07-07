import push
from datetime import datetime
from pytz import timezone
import logging



def finaltext(header,posted,attention,url):
    logging.info("Inside final text") 
    ist = timezone('Asia/Kolkata')
    try:
        logging.info("Making the text")
        text= str(datetime.now(ist).strftime("%d-%m-%Y %H:%M:%S ")) + "\n" + "Titled: "+ str(header) +"\n" + "Posted by: " + str(posted) +"\n" +"For:  " + str(attention) + " \n"
    except Execption as e:
        logging.error("creating text failed %s",e)
    try:
         logging.info("sending text to push")
         push.push(text,url)
    except Exception as e:
        logging.error("Calling push failed %s",e)
      


if __name__ == "__main__":
    log_level = logging.DEBUG
    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s()\t%(message)s"
    logging.basicConfig(format=log_format, level=log_level) 
