import requests
import json

# GitHub repository details
owner = 'your-github-username'
repo = 'your-repo-name'
workflow_id = 'your-workflow-id'  # Can be the workflow file name or its ID
token = 'your-github-token'

# Triggering the workflow
url = f'https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
data = {
    'ref': 'main',  # Branch to run the workflow on
    'inputs': {}  # Optional: inputs for the workflow
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 204:
    print('Workflow triggered successfully.')
else:
    print(f'Failed to trigger workflow: {response.status_code}')
    print(response.text)
