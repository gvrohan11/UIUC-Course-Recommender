import rmp
from transformers import pipeline

#input must be valid json object from get_prof_info output
def get_sentiment(prof_json):
    num_comments = 0
    pos_comments = 0
    sentiment_pipeline = pipeline('sentiment-analysis')
    for key in prof_json.keys():
        for comment in prof_json[key]['comments']:
            #print(comment, sentiment_pipeline(comment))
            if sentiment_pipeline(comment)[0]['label'] == 'POSITIVE':
                pos_comments+=1
            num_comments+=1
    return round(pos_comments/num_comments, 3) * 100 #returns percentage of positive comments


print(get_sentiment(rmp.get_prof_info("1112", "Alexei Stepanov")))