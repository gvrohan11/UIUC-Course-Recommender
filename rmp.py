
import requests
import re
import json
import base64
import os
from bs4 import BeautifulSoup

import pandas as pd


# uiuc id  = [1112]

# def get_tid(name: str):

#     id = "1112"
#     url = "https://www.ratemyprofessors.com" \
#           "/search/teachers?query=%s&sid=%s" % (name, base64.b64encode(("School-%s" % id)
#                                                                                  .encode('ascii')).decode('ascii'))
#     page = requests.get(url)
#     tid = re.findall(r'"legacyId":(\d+)', page.text)
#     return tid
    



def get_prof_info(id : str, professor_name: str):
    url = "https://www.ratemyprofessors.com" \
          "/search/teachers?query=%s&sid=%s" % (professor_name, base64.b64encode(("School-%s" % id)
                                                                                 .encode('ascii')).decode('ascii'))
    page = requests.get(url)
    tid = re.findall(r'"legacyId":(\d+)', page.text)
    if len(tid) == 0:
        return {}
    result = {}
    for i in range(len(tid)):
        url2 = f"https://www.ratemyprofessors.com/professor?tid={tid[i]}"
        teacher_page = requests.get(url2)
        soup = BeautifulSoup(teacher_page.content, 'html.parser', from_encoding="utf-8")
        overall = soup.find_all("div", {"class": "RatingValue__Numerator-qw8sqy-2 liyUjw"})[0].text 
        would_take = soup.find_all("div", {"class": "FeedbackItem__FeedbackNumber-uof32n-1 kkESWs"})[0].text 
        difficulty =  soup.find_all("div", {"class": "FeedbackItem__FeedbackNumber-uof32n-1 kkESWs"})[1].text
        num_ratings =  soup.find_all('a', href="#ratingsList")[0].text.split()[0]
        name = soup.find_all("div", {"class": "NameTitle__Name-dowf0z-0 cfjPUG"})[0].text
        dept =  soup.find_all("div", {"class": "NameTitle__Title-dowf0z-1 iLYGwn"})[0].text   
        d1 = re.findall(r"(?<=Professor in the ).*$", dept)
        d2 = re.findall(r".*?(?= department)", d1[0])[0]
        d2 = d2.rstrip()
        name = name.rstrip()

        raw_comment_list = soup.find_all("div",{"class": "Comments__StyledComments-dzzyvm-0 gRjWel"})
        comments = []
        for raw_comment in raw_comment_list:
            comments.append(raw_comment.text)
    

        result[tid[i]] = {"name": name,  "overall": overall, "would_take":would_take, "difficulty": difficulty, "num_ratings":num_ratings, "dept": d2, "comments": comments}
    return result
   


#a = get_prof_info("1112", "Graham Evans")
#print(a)

#ADD RMP DATA TO COURSE GPA CSV
""" course_df = pd.read_csv("all_courses_gpa.csv")
course_df['Rate My Professor'] = 0
rating_map = {}
for index, row in course_df.iterrows():
    prof_name = row['Primary Instructor']
    if not pd.isna(prof_name):
        name = prof_name[prof_name.find(', ')+2:] +" "+ prof_name[:prof_name.find(', ')]
        without_initial_arr = re.split('[A-Z]\s[A-Z]',name) #want to remove middle initial
        #print(without_initial_arr)
        if len(without_initial_arr)>1:
            name = without_initial_arr[0] + name[ (name.find(without_initial_arr[1])-1) : ]

        
        #print(name)
        if (name not in rating_map.keys()):
            try:
                #print(get_prof_info(1112, name))
                response = get_prof_info(1112, name)
                if len(response) == 0:
                    course_df.at[index, 'Rate My Professor'] = "Not Found"
                    rating_map[name] = "Not Found"
                    print("failed at "+name)
                else:
                    course_df.at[index, 'Rate My Professor'] = response
                    rating_map[name] = response
                    print("successful at "+name)
                    
            except:
                course_df.at[index, 'Rate My Professor'] = "Not Found"
                rating_map[name] = "Not Found"
                print("failed at "+name)
        else:
            course_df.at[index, 'Rate My Professor'] = rating_map[name] 
            print("already found "+name)

print(course_df)
course_df.to_csv("check_course_rmp.csv") """

