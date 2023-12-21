# import psaw

import pandas as pd
import re
import warnings
warnings.filterwarnings("ignore")
from dateutil import tz
from psaw import PushshiftAPI

subr = 'UIUC'
link = 'z5b55r'

api = PushshiftAPI()
# Set display
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
url = 'https://www.reddit.com/r/UIUC/comments/z5b55r/places_that_are_open_24hrs/'
sub_match = re.findall(r'/r/\.?([ \d\w.]+)', url)
post_id_match = re.findall(r'/comments/\.?([ \d\w.]+)', url)
subreddit = sub_match[0]
post_id = post_id_match[0]
print('\nFetching comments now :)')
gen = api.search_comments(subreddit=subr, link_id=link)
max_response_cache = 1000
cache = []
for c in gen:
    cache.append(c)
# Omit this test to actually return all results. Wouldn't recommend it though: could take a while, but you do you.
    if len(cache) >= max_response_cache:
        break
# If you really want to: pick up where we left off to get the rest of the results.
if False:
    for c in gen:
        cache.append(c)
        
df = pd.DataFrame([thing.d_ for thing in cache])
df_comments = df[['author','created', 'body']]
df_time_cleaned = df_comments.copy()
df_time_cleaned['created'] = pd.to_datetime(df_time_cleaned['created'], unit = 's', utc=True).dt.tz_convert('Asia/Singapore')
df_time_cleaned = df_time_cleaned.sort_values(by='created', ascending=False)
df_final = df_time_cleaned
print('\nTotal comments fetched from post:',len(df_final['body']))
df_final