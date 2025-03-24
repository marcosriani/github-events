import requests
import datetime


def get_github_data(github_username):
    try:
        response = requests.get(f"https://api.github.com/users/{github_username}/events")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching GitHub data: {err}")
        return []

def format_date(date_str):
    """Format GitHub date string to a more readable format."""
    created_date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return f"Created at: {created_date.strftime('%A, %B %d, %Y at %I:%M %p')}"

def display_event(event):
    """Display formatted event information."""
    print("\n")
    print(f"Username: {event['actor']['login']}")
    print(f"Type: {event['type']}")
    print(f"Created at: {format_date(event['created_at'])}")
    print(f"Repository: {event.get('repo', {}).get('name', 'N/A')}")
    if event['type'] == 'PushEvent':
        for commit in event.get('payload', {}).get('commits', []):
            print(f"Commit message: {commit.get('message', 'N/A')}")
    else:
        print("Commit message: N/A")

user_username = input("Github username: ")
github_events = get_github_data(user_username)

for github_event in github_events:
    display_event(github_event)