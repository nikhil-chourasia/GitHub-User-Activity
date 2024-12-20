from github import Github
from github import Auth
from github import GithubException

auth = Auth.Token("access_token")
g = Github(auth=auth)

username = input("Enter your GitHub username here: ").strip()

try:

    user = g.get_user(username)
    print("User Details:")
    print(f"Name = {user.name}")
    print(f"Bio: {user.bio}") 
    print(f"Location: {user.location}") 
    print(f"Public Repos: {user.public_repos}") 
    print(f"Followers: {user.followers}") 
    print(f"Following: {user.following}")

    events = g.get_events()
    for event in events:
        eventType = event.type
        repoName = event.repo.name
        if eventType == "PushEvent":
            commitCount = len(event.payload['commits'])
            print(f"{username} has made {commitCount} commits in {repoName}")       

except GithubException as e:
    if e.status == 404:
        print("Error: User not Found! :(")
    elif e.status == 403:
        print("Error: Server rate limit exceeded! :(")
    else: 
        print(f"Failed to fetch Activity as {e}")

except Exception as e:
    print(f"An unexpected error occured: {e}")
