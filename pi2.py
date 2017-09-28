#programing to tweet pictures useing raspberry pie
from TwitterAPI import TwitterAPI#twitter api

CONSUMER_KEY = ''#acount details 
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''#account details
b=1

while True:#creates a while loop
    b=b+1
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open('/home/pi/cam/imgs/'+str(b)+'.jpg', 'rb')
    print('done')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
    print(r.status_code)
