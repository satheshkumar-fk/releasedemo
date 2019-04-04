from jira import JIRA
from jira.exceptions import JIRAError
import sys
import os
import netrc

def jira_auth(url, username, password):
    try:
        jira = JIRA(url, basic_auth=(username, password))
        print ("Logged in successfully!")
        return jira
    except JIRAError as e:
        if e.status_code == 401:
            print ("Login to JIRA failed. Check your username and password!")

def fetch_jira_message(jira,ticket):
    try:
        issue = jira.issue(ticket)
        summary = issue.fields.summary
        desc = issue.fields.description
        print (desc)
        jira_url = 'https://fourkites.atlassian.net/browse/' + ticket
        print (jira_url, summary)
        commit_msg = jira_url + ' ' +summary
        return commit_msg
    except JIRAError as err:
        print ("Issue does not exist or you do not have permission to see it!")
        return

def write_commit_message(message):
    path = os.getcwd()
    filename = path + '/' + '.commit_msg'
    fp = open(filename, 'w')
    fp.write(message)
    fp.close()

def main():
    machine = sys.argv[1]
    n = netrc.netrc()
    authTokens = n.authenticators(machine)
    username = authTokens[0]
    url = authTokens[1]
    password = authTokens[2]
    ticket = sys.argv[2]
    jira = jira_auth(url, username, password)
    commit_message = fetch_jira_message(jira, ticket)
    write_commit_message(commit_message)

if __name__ == "__main__":
  main()
