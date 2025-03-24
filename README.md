```markdown
# GitHub Event Viewer

This simple Python script fetches and displays recent events from a GitHub user's profile using the GitHub API.

## Features

- Fetches recent events from a specified GitHub user.
- Displays event details such as username, event type, creation date, repository name, and commit messages (if applicable).

## Requirements

- Python 3.x
- `requests` library

You can install the required library using pip:

```bash
pip install requests
```

## Usage

1. Run the script.
2. Enter the GitHub username when prompted.
3. The script will display the recent events associated with the specified user.

## Functions

- `get_github_data(github_username)`: Fetches event data from the GitHub API for the specified user.
- `format_date(date_str)`: Formats the GitHub date string into a more readable format.
- `display_event(event)`: Displays formatted event information.

## Example

```bash
Github username: octocat
```

The script will output the recent events for the user `octocat`.

## Note

- Ensure you have an active internet connection to fetch data from the GitHub API.
- The script handles HTTP errors gracefully and prints an error message if the data cannot be fetched.

project URL: [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/github-user-activity)
```

