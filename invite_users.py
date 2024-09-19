import os
import requests

# Replace with the organization name
ORG_NAME = 'DeepakRavula'
# Replace with the repository name
REPO_NAME = 'SMW-D'

# List of interns to invite with their GitHub usernames
interns = [
    'Deepak2202-del',
]

def invite_user(username, token):
    # API endpoint to invite collaborator to the repository
    url = f'https://api.github.com/repos/{ORG_NAME}/{REPO_NAME}/collaborators/{username}'
    
    # Headers for authentication
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Payload for the invitation
    data = {
        'permission': 'admin'  # Permissions can be 'pull', 'push', or 'admin'
    }

    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'Successfully invited {username}')
    elif response.status_code == 204:
        print(f'{username} is already a collaborator')
    else:
        print(f'Failed to invite {username}: {response.status_code}, {response.json()}')

def main():
    # Read token from environment variable
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN is not set in environment variables.")
        return

    for intern in interns:
        invite_user(intern, GITHUB_TOKEN)

if __name__ == "__main__":
    main()


# export GITHUB_TOKEN=your_personal_access_token
