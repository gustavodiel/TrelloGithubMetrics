# Trello Metrics

The objective of this repo is to have a nice little script that may fetch data from a [Trello](https://Trello.com) board, and within a certain list, fetch all the **Pull Requests** that are attached to the cards. With all those PRs, the script will also fetch all the info related to the PR and display like this:
```
Cards in Done: 169
PRs in Done: 179
Added lines: 20127
Removed lines: 7029
Added lines on master: 16483
Removed lines on master: 6199
Created commits: 1523
Total files changed: 366 (The full list can be found here: https://gist.github.com/USER/CREATED_GIST)
```

## Requirements
- Python 3
- Pips: `pip install py-trello PyGithub`

## Configuring
- First, open metrics.py and replace the following constants:
- **CREATE_GIST**: Whether or not you want the metrics to create a gist containing all the files the PRs have created/modified/deleted
- **PUBLIC_GIST**: Whether or not the gist created form above is public
- **TRELLO_BOARD_NAME**: The board in your Trello's accout. Must be exact!
- **TRELLO_LIST_NAME**: The name of the list in the board above. Must be exact!
- **TRELLO_TOKEN**: Use the link [here](https://trello.com/app-key/) and press on `Generate Token`.
- **TRELLO_KEY**: You may generate one [here](https://trello.com/app-key/).
- **GITHUB_ACCES_KEY**: You may generate one [here](https://github.com/settings/tokens).
  - The token must have the following accesses:
    - Full control of private repositories (needed)
    - Create Gists (only if you set **CREATE_GIST** to `True`)

With all that done, just run it!

## Running
```sh
python metrics.py
```
