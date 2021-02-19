# Python 3.7.3

import requests
import os
import sys
import subprocess


def Main(repoName):
    # Github API URL
    API_URL = "https://api.github.com"
    # Web URL to user's Github page
    USER_URL = "https://github.com/user"
    # Path to projects directory
    projectPath = "path/to/projects/folder"
    # Created repo directory
    repoPath = f"{ projectPath }/{ repoName }"
    # Github auth token stored in environment variable as GITHUB_TOKEN
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    # Data for API to create repo
    data = "{\"name\": \"" + repoName + "\"}"
    # Authentication for API
    headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Creates repo
        requests.post(f"{ API_URL }/user/repos", data=data, headers=headers)

        print("\n======================================")
        print("Repository has been successfully made!")
        print("======================================\n")

        try:
            # Creates repo directory on system
            os.makedirs(f"{ repoPath }")

            # Command-line process creates README.md
            subprocess.call(
                ["touch", "README.md"],
                cwd=repoPath
            )

            # Command-line process creates .gitignore
            subprocess.call(
                ["touch", ".gitignore"],
                cwd=repoPath
            )

            # Command-line process initialises github repo
            subprocess.call(
                ["git", "init"],
                cwd=repoPath
            )

            # Command-line process adds README.md and .gitignore
            subprocess.call(
                ["git", "add", "--all"],
                cwd=repoPath
            )

            # Command-line process commits README.md and .gitignore
            subprocess.call(
                ["git", "commit", "-m", "\"init commit\""],
                cwd=repoPath
            )

            # Command-line process creates a remote connection with github repo
            subprocess.call(
                [
                    "git", "remote", "add",
                    "origin", f"{ USER_URL }/{ repoName }.git"
                ],
                cwd=repoPath
            )

            # Command-line process updates repo with changes
            subprocess.call(
                ["git", "push", "-u", "origin", "master"],
                cwd=repoPath
            )

            # File explorer doesn't like / used in paths
            repoPath = repoPath.replace('/', '\\')

            # Command-line process opens file explorer in repo directory
            subprocess.call(f"explorer \"{ repoPath }\"")

            print("\n=======================================")
            print("Folders and files successfully created!")
            print("=======================================\n")
        except FileExistsError:
            print("\n===============================")
            print("Unable to folders and or files!")
            print("===============================\n")
    except requests.exceptions.RequestException:
        print("\n============================")
        print("Unable to create repository!")
        print("============================\n")


if __name__ == "__main__":
    # Checks for no arguments
    try:
        Main(str(sys.argv[1]))
    except IndexError:
        print("\n==========================================")
        print("You have improperly named your repository!")
        print("==========================================\n")
