# course-project-group-99

## a. Summary of Presentation Introduction

We wanted to create a comprehensive rating platform tailored toward the courses and professors at UIUC. We consolidated ratings from "Rate My Professors" and Reddit, as well as course GPAs, in order to provide students with a broad overview of their course workload and difficulty. This involved the generation of course-specific metrics that incorporated NLP sentiment analysis and class section GPA to provide students with a recommendation about their inputted course.

## b. Describes Technical Architecture
First we used Professor Wade Fagen-Ulmschneider's GPA dataset from github, and then we manually computed (using pandas) the average GPA column. To be able to use the data effectively in Flask, we converted the entire CSV file into a well-formatted JSON structure. Then we used this dataset as the list of courses that users can select from in the home-webpage by using jquery's autocomplete feature. After the user has selected all their courses, they can press a button to generate a recommendation. The selected courses get sent to a hidden route that handles Post requests. The route then returns the data to Flask, where the data is  processed using the ratemyprof functions and the sentiment analysis functions. This data is then sent to another flask route that displays the selected courses and the information we obtained on them, and also generates a recommendation based on the overall score.

## c. Provides Reproducible Installation Instruction
### We require you to have the following libraries installed: 
	json, rmp, flask, transformers, requests, re, base64, bs4
### Note that to run flask you may need to use one of the following commands (this depends on where you install flask):
	flask --app app --debug run
  	
	python -m flask --app app --debug run
 	
	python3 -m flask --app app --debug run

	By default the flask server will run on http://127.0.0.1:5000/ and this will be hyperlinked in the terminal 


## d. Group members and Their roles
### Daniyal:
Built course GPA dataset and created the sentiment analysis scripts
### Aditya:
   Built the front-end and the RateMyProf functions
### Deepit:
   Worked on getting the user input, building proposals, and identified which APIs are needed for NLP
### Rohan

