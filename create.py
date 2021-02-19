import requests
import os
import sys
import subprocess


def Main(repoName):
    API_URL = "https://api.github.com"
    USER_URL = ""
    projectPath = "path/to/projects/folder"
    repoPath = f"{ projectPath }/{ repoName }"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    data = "{\"name\": \"" + repoName + "\"}"
    headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        requests.post(f"{ API_URL }/user/repos", data=data, headers=headers)

        print("\n======================================")
        print("Repository has been successfully made!")
        print("======================================\n")

        try:
            os.makedirs(f"{ repoPath }")

            subprocess.call(
                ["touch", "README.md"],
                cwd=repoPath
            )

            subprocess.call(
                ["touch", ".gitignore"],
                cwd=repoPath
            )

            subprocess.call(
                ["git", "init"],
                cwd=repoPath
            )

            subprocess.call(
                ["git", "add", "--all"],
                cwd=repoPath
            )

            subprocess.call(
                ["git", "commit", "-m", "\"init commit\""],
                cwd=repoPath
            )

            subprocess.call(
                [
                    "git", "remote", "add",
                    "origin", f"{ USER_URL }/{ repoName }.git"
                ],
                cwd=repoPath
            )

            subprocess.call(
                ["git", "push", "-u", "origin", "master"],
                cwd=repoPath
            )

            repoPath = repoPath.replace('/', '\\')

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
    try:
        Main(str(sys.argv[1]))
    except IndexError:
        print("\n==========================================")
        print("You have improperly named your repository!")
        print("==========================================\n")
