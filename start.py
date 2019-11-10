from github import Github
import sys
import os


path = "/Users/malcolmherbert/Documents/Charlie/Projects/MyProjects"
username = "your github username"
password = "your github password"


def start():
    projectName = str(sys.argv[1])
    os.makedirs(path + str(projectName))

    user = Github(username, password).get_user()
    repo = user.create_repo(str(projectName))
    print("\n======================================")
    print("Repository has been successfully made!")
    print("======================================\n")


if __name__ = '__main__':
    start()
