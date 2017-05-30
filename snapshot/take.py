#!/usr/bin/env python


import requests

def getRepos(org_name):
    """Takes an organization name as input and returns either a list of public Github repos (including an empty list
    if there are none) or an error code."""

    response = requests.get('https://api.github.com/orgs/' + org_name + '/repos')
    if response.status_code == 200:
        repos = response.json()
        repo_list = [repo['name'] for repo in repos if not repo['private']]
        return repo_list
    else:
        return response.status_code