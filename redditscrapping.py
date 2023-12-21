import requests
import pandas as pd
import schedule
import csv

personal_use_script = 'cvubelfv0g5PXYiRhaI7Cg'
secret_token = 'Ie9ukcv-IrwwqAal35AKCXVQvHQDcg'

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
# auth = requests.auth.HTTPBasicAuth('<CLIENT_ID>', '<SECRET_TOKEN>')
auth = requests.auth.HTTPBasicAuth(personal_use_script, secret_token) # 

# here we pass our login method (password), username, and password
'''
data = {'grant_type': 'password',
        'username': '<USERNAME>',
        'password': '<PASSWORD>'}
'''
data = {'grant_type': 'password',
        'username': 'rohanvg3',
        'password': 'Ramxj#275'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'CourseRecommender/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

to_print = f'Access Token Value = {TOKEN} \n'
print(to_print)

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# this is the entire map / dictionary of requests we get from the hot tab of UIUC reddit
res = requests.get("https://oauth.reddit.com/r/UIUC/hot",
                   headers=headers) # new, top

# printing out the map
# print(res.json()['data']['children'])

num = 1
for post in res.json()['data']['children']:
        stuff = post['data']['title']
        to_pr = f'{num}: {stuff} \n'
        print(to_pr)
        body = post['data']['selftext']
        to_pr2 = f'{num}: {body} \n'
        print(to_pr2)
        num += 1

print("-------------------------------------------------\n")

# for testing only
def get_num_reddit_titles():
        num = 1
        for post in res.json()['data']['children']:
                stuff = post['data']['title']
                to_pr = f'{num}: {stuff} \n'
                print(to_pr)
                num += 1
        return num



df = pd.DataFrame()

for post in res.json()['data']['children']:
  # Creating a DataFrame
  df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)

df.head()


# Create a csv file
# Create script to run code every 2 hours
# every time the script runs, retireve the 27 posts
# update / add those 27 posts to the CSV
# separate the chunks of updated posts by a line
# add the date and time the code is ran and uploaded to the csv file