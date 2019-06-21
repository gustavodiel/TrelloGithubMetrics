# Trello Metrics

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
