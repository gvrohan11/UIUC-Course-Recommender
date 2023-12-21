import asyncpraw
import pandas as pd
#from dateutil import tz

'''
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="Comment Extraction (by u/USERNAME)",
    username="USERNAME",
)
'''

CLIENT_ID = "cvubelfv0g5PXYiRhaI7Cg"
CLIENT_SECRET = "Ie9ukcv-IrwwqAal35AKCXVQvHQDcg"
PASSWORD = "Ramxj#275"
USERNAME = "rohanvg3"

reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent="Comment Extraction (by u/USERNAME)",
    username=USERNAME,
)

subreddit = reddit.subreddit("UIUC")

top_posts = subreddit.top(limit=1) #100

def getComments(class_name):
  other_string = ''
  if class_name[-4] == ' ':
    other_string = class_name[0:-4] + class_name[-3:len(class_name)]
  else:
    other_string = class_name[0:-3] + ' ' + class_name[-3:len(class_name)]
  
  # retrieve ALL POSTS
  # retrieve ALL URLS
  # Get comments with URL ting

  i = 0
  for submission in top_posts:
    # if not submission.stickied:
    if (class_name in submission.title) or (other_string in submission.title):
      title = f'{i} Title: {submission.title} \n'
      print(title)
      #print(submission)
      comments = submission.comment
      for comment in comments:
        print(comment)
      i += 1



  # df = pd.DataFrame([thing.d_ for thing in cache])
  # df_comments = df[['created', 'body']]
  # df_time_cleaned = df_comments.copy()
  # df_time_cleaned['created'] = pd.to_datetime(df_time_cleaned['created'], unit = 's', utc=True).dt.tz_convert('Asia/Singapore')

  # Search by keyword within reddit (subreddit.keyword())
  # retrieve all their ruls
  # get comments w each URL

# print(getComments('CS124'))
# print(getComments('CS 124'))

getComments('CS 124')