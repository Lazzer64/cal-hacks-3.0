import requests
import requests.auth
from search import *
from analysis import *

auth = open('auth','r') # file named auth with clientid on first line and secret on second line
clientID   = auth.readline()[:-1]
secret     = auth.readline()[:-1]
watson_cid = auth.readline()[:-1]
watson_sec = auth.readline()[:-1]

username   = raw_input('Enter Reddit username: ')
username   = str(username)

client_auth = requests.auth.HTTPBasicAuth(clientID,secret)
post_data   = {'grant_type':'client_credentials'}
headers     = {'User-Agent': 'client'}
response    = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers).json()

token      = response['access_token']
token_type = response['token_type']

sort      = 'top' # hot, new, top, controversial
t         = 'all' # hour, day, week, month, year, all
params    = {'limit':'100', 'sort':sort, 't':t}
headers   = {'Authorization': token_type+' '+token, 'User-Agent': 'client'}
response  = requests.get('https://oauth.reddit.com/user/'+username+'/comments', headers=headers, params=params).json()

posts = response.get('data')
texts = []
for post in posts.get('children'):
    texts.append(post.get('data').get('body').encode('utf-8'))

personality(texts, (watson_cid, watson_sec))
