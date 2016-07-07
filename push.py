import json
import requests
import logging
def push(body,url):
    try:
        logging.info("Pushing....the message")
        push_url = "https://api.pushbullet.com/v2/pushes"
        auth_token = 'bfRDUwDWZUyC2BYUnxEZL6OVy5mhFA3B'
        channel_tag = 'iiitbhna'
        title="Notice Alert..!"
        auth = requests.auth.HTTPBasicAuth(auth_token, '')
        headers = {'content-type' : 'application/json'}
        payload = {}
        payload['type'] = 'link'
        payload['url'] = url
        payload['title'] = title
        payload['body'] = body
        payload['channel_tag'] = channel_tag
        data = json.dumps(payload)
        response = requests.post(push_url, auth=auth, headers=headers,
			data=data)
    except Exception as e:
        logging.error("Pushing failed %s",e)
    
    
if __name__ == "__main__":
    log_level = logging.DEBUG
    log_format = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s()\t%(message)s"
    logging.basicConfig(format=log_format, level=log_level) 
   
        
