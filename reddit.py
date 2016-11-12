import requests
import requests.auth
from search import *

auth = open('auth','r') # file named auth with clientid on first line and secret on second line
clientID = auth.readline()[:-1]
secret   = auth.readline()[:-1]
username = 'covie21'

client_auth = requests.auth.HTTPBasicAuth(clientID,secret)
post_data   = {'grant_type':'client_credentials'}
headers     = {'User-Agent': 'client'}
response    = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers).json()

token      = response['access_token']
token_type = response['token_type']

headers   = {'Authorization': token_type+' '+token, 'User-Agent': 'client'}
response  = requests.get('https://oauth.reddit.com/user/'+username+'/comments', headers=headers, params={'limit':'100'}).json()

posts = response.get('data')

# from IPython import embed
# embed()

texts = []
for post in posts.get('children'):
    texts.append(post.get('data').get('body'))

excluded = ['a', 'and', 'or', 'the', 'if', 'i', 'when', 'to']
results = search(texts, excluded)
print len(texts)
for item in results:
    print item

