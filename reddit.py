import requests
import requests.auth

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

headers  = {'Authorization': token_type+' '+token, 'User-Agent': 'client'}
response = requests.get('https://oauth.reddit.com/user/'+username+'/comments', headers=headers).json()

posts = response.get('data')

list = []
for post in posts.get('children'):
    list.append(post.get('data').get('body'))
