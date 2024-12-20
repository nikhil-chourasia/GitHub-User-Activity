# GitHub User Info Fetcher 🚀

This script fetches details and recent activity for a specified GitHub user using the GitHub API. It utilizes the `PyGithub` library to interact with the API.

## Features ✨
- Retrieves user details such as name, bio, location, public repositories, followers, and following.
- Fetches the latest events for the user and displays commit counts for `PushEvent`s.
- Handles common errors, such as user not found or API rate limits.

## Prerequisites ✅
Before using the script, ensure you have the following:

1. Python 3.6 or later installed. 🐍
2. The `PyGithub` library installed. You can install it using pip:
   ```
   pip install PyGithub
   ```
3. A GitHub personal access token for authentication. 🔑 Learn how to create a token [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Usage 🛠️
1. Clone the repository or download the script. 📂
2. Replace `"access_token"` in the script with your actual GitHub personal access token. 🔒
3. Run the script:
   ```
   python script_name.py
   ```
4. Enter a GitHub username when prompted. 🧑‍💻

## Example 📋
### Input
```
Enter your GitHub username here: octocat
```

### Output
```plaintext
User Details:
Name = The Octocat
Bio: GitHub mascot
Location: San Francisco
Public Repos: 8
Followers: 100
Following: 0

octocat has made 5 commits in octocat/Hello-World
```

## Error Handling ⚠️
The script handles the following errors:
1. **User Not Found (404):** Displays an error message if the username doesn't exist. ❌
2. **Rate Limit Exceeded (403):** Alerts you if the server's API rate limit is exceeded. 🚫
3. **Unexpected Errors:** Prints details of any unexpected errors. 🛑

## Notes 📝
- Replace `"access_token"` with your actual token to avoid authentication issues. 🔐
- The `get_events()` method may require elevated permissions depending on the visibility of the user's activity. 🔍

## License 📜
This project is licensed under the MIT License. Feel free to use, modify, and distribute the script. 👍

## Project URL 📂
The Project Guidelines and Problems are taken from https://roadmap.sh/projects/github-user-activity 🔗


---
For any issues or suggestions, please feel free to raise an issue or create a pull request! 🤝
