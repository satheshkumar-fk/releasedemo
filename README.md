# releasedemo

Release Process:

    Release process currently has 2 python scripts and 2 shell scripts
    
    1. Fecthing the summary from the relevant jira (fetch_jira_desc.py)
    
        Ex: Jira - https://fourkites.atlassian.net/browse/AM-121
            Summary - Company master to global master mapping
            
    2. Commit Message Enforement Hook (commit-msg.py) which enforces the commit message format
    
    3. Shell script (install_commit_msg_hook.sh) to install the hook
    
    4. Shell script (git_commit.sh) to commit the changes and remove the .commit_msg file
    
    Requirements:

        1. Python3 - Installed in the machine (If not try brew install python3)
        2. JIRA Python package - If not insatlled use pip3 install jira
        
    Steps:
    
        1. First setup a .netrc file under your local machine home directory. This file will be used to store the JIRA credentials which used for fetching the desc.
        
            SatheshK-223:~ sathesh$ vi ~/.netrc
            
        2. Paste the below content in the .netrc file. Replace the password with correct value and save the file
        
            machine FK223
            account https://fourkites.atlassian.net
            login release@fourkites.com
            password xxxxxxxxxxxxxxxxxxxxx
            
        3. Execute the shell script which installs the hook
        
            This script will simply copy the commit-msg.py python file into the hooks directory ($HOME_DIR/.git/hooks/commit-msg) and make it executable
            
            SatheshK-223:~ sathesh$chmod +x install_commit_msg_hook.sh && ./install_commit_msg_hook.sh
            
        4. Now the hook is installed, utilise the fetch_jira_desc.py to pull the summary information from JIRA. This script needs your local machine name and JIRA issue as parameters
        
            SatheshK-223:~ sathesh$python3 fetch_jira_desc.py FK223 AM-121
            
        5. The Fetched JIRA summary will be stored in the .commit_msg under the project home folder
        
        6. Execute the git_commit.sh to commit the changes
        
    Note: If the user want to overide the commit hook use the -n or --no-verify option
    
        Ex: SatheshK-223:~ sathesh$git commit -n "First Commit"