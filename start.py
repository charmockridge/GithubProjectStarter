from github import Github
import sys
import os


path = "/Users/edit/path/to/match/your/own/"
username = "your github username"
password = "your github password"

projectName = str(sys.argv[1])
os.makedirs(path + projectName)

user = Github(username, password).get_user()
user.create_repo(str(projectName))

print("\n======================================")
print("Repository has been successfully made!")
print("======================================\n")
