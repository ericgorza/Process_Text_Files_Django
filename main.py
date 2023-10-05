import os
import requests

url = "http://<replace with the IP>/feedback"  #replace the external ID 34.30.6.247 - for the exercise
files_directory = "your_directory" #/data/feedback - for the exercise

text_files_path = os.listdir(files_directory)

text_files_list = []

for file in text_files_path:
    text_files_list.append(file)

file_path_list = []

for name in text_files_list:
    file_path = os.path.join(files_directory,name)
    file_path_list.append(file_path)

dict_feedbacks = {}

for f in file_path_list:
    with open (f,"r") as text_reader:
        content = text_reader.readlines()
        title = content[0].strip("\n")
        name = content[1].strip("\n")
        date = content[2].strip("\n")
        feedback = content[3]
        dict_feedbacks["title"] = title
        dict_feedbacks["name"] = name
        dict_feedbacks["date"] = date
        dict_feedbacks["feedback"] = feedback

    requests.post(url=url, json=dict_feedbacks)

response = requests.post(url=url, json=dict_feedbacks)
if response.status_code == 201:
    print("Feedback sent.")
else:
    print(f"Error: {response.status_code}.")

## I wrote this code super quickly,
# I could've created one dictionary and appended it to a list of dictionaries
# to make the code more efficient.