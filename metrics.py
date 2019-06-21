#! /bin/usr/env python3

from trello import TrelloClient
from github import Github, InputFileContent
import re

# CONFIGURATIONS #

# Application:
CREATE_GIST = False
PUBLIC_GIST = False


# Trello Stuff:
TRELLO_BOARD_NAME = ''  # Exact name!
TRELLO_LIST_NAME = 'Done'  # Exact name!


# This kes you may find on https://trello.com/app-key/. The keys will appear there, and for the Token,
# press "Generate Token".
TRELLO_TOKEN = ''
TRELLO_KEY = ''


# Github keys. Get from https://github.com/settings/tokens. Need access to:
# Full control of private repositories
# Create Gists (if you want)
GITHUB_ACCESS_KEY = ''

########################


client = TrelloClient(api_key=TRELLO_KEY, api_secret=TRELLO_TOKEN)
github = Github(GITHUB_ACCESS_KEY)

user = github.get_user()

boards = client.list_boards()

desired_board = list(filter(lambda board: board.name == TRELLO_BOARD_NAME, boards))[0]

desired_list = list(filter(lambda curr_list: curr_list.name == TRELLO_LIST_NAME, desired_board.list_lists()))[0]

cards = desired_list.list_cards()

attaches = list(map(lambda card: card.attachments, cards))

flattened = [item for sublist in attaches for item in sublist]

github_urls = list(map(lambda attachment: attachment['url'], flattened))

repos = {}

total_aditions = 0
total_deletions = 0

real_total_aditions = 0
real_total_deletions = 0

paginated_files = []
files_changed = []
commit_num = 0

prs = []


def extract_pr_data(url):
    if 'pull' in url:
        match_pr = re.search("(\d+)$", url)
        match_repo = re.search(".com/(\S+)/.*/", url)
        return match_pr.string[match_pr.start():match_pr.end()], match_repo.groups()[0]
    return


def fetch_repo(repo_name):
    if repo_name not in repos:
        repos[repo_name] = github.get_repo(repo_name)
    return repos[repo_name]


for github_url in github_urls:
    result = extract_pr_data(github_url)
    if result:
        (pr_id, repo_name) = result
        repo = fetch_repo(repo_name)
        pr = repo.get_pull(int(pr_id))
        prs.append(pr)
    else:
        print("Found a non-PR link: " + github_url)

for pr in prs:
    total_aditions += pr.additions
    total_deletions += pr.deletions
    paginated_files.append(pr.get_files())
    commit_num += pr.commits
    if pr.merged:
        real_total_aditions += pr.additions
        real_total_deletions += pr.deletions

for paginated_file in paginated_files:
    page_index = 0
    files = paginated_file.get_page(page_index)
    while len(files) != 0:
        [files_changed.append(file.filename) for file in files]
        page_index += 1
        files = paginated_file.get_page(page_index)

uniq = list(set(files_changed))
uniq.sort()

gist_url = None

if CREATE_GIST:
    files = {'list_of_files.txt': InputFileContent('\n'.join(uniq))}
    gist_url = user.create_gist(public=PUBLIC_GIST, description='Files that have been changed', files=files).html_url

gist_print_string = ''

if gist_url:
    gist_print_string = '(The full list can be found here: {})'.format(gist_url)

print(
    """
    Cards in Done: {}
    PRs in Done: {}
    Added lines: {}
    Removed lines: {}
    Added lines on master: {}
    Removed lines on master: {}
    Created commits: {}
    Total files changed: {} {}
    """.format(len(cards), len(prs), total_aditions, total_deletions, real_total_aditions, real_total_deletions, commit_num, len(uniq), gist_print_string)
)
