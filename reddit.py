import requests
import requests.auth
from search import *

auth = open('auth','r') # file named auth with clientid on first line and secret on second line
clientID = auth.readline()[:-1]
secret   = auth.readline()[:-1]
username = raw_input('Enter your name: ')
username = str(username)
numResults = raw_input('Return how many? ')
numResults = int(numResults)

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

# from IPython import embed
# embed()

texts = []
for post in posts.get('children'):
    texts.append(post.get('data').get('body'))

excluded = ['a', 'and', 'or', 'the', 'if', 'i', 'when', 'to', 'in', 'for',
    'it', 'on', 'his', 'her', 'he', 'she', 'they', 'their', 'your', 'us', 'our',
    'do', 'more', 'was', 'were', 'be', 'is', 'are', 'but', 'you', 'so', 'not',
    'of', "it's", 'its', 'this', 'that', 'why', 'how', 'who', 'what', 'when',
    'as', 'has', 'had', 'have', 'my', 'with', 'could', 'should', 'would']
results = search(texts, excluded, numResults)
for item in results:
    print item
