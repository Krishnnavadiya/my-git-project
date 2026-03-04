# git remote -v
# git branch -M main         
# git remote add origin https://github.com/Krishnnavadiya/my-git-project.git
# git push -u origin main

# Enumerating objects: 17, done.
# Counting objects: 100% (17/17), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (12/12), done.
# Writing objects: 100% (17/17), 1.61 KiB | 826.00 KiB/s, done.
# Total 17 (delta 4), reused 0 (delta 0), pack-reused 0
# To https://github.com/Krishnnavadiya/my-git-project.git
#  * [new branch]      main -> main
# branch 'main' set up to track 'origin/main'.

# git checkout -b feature-greeting
# Switched to a new branch 'feature-greeting'

# Create new file which have a new feature (feature.py)

# git add feature.py
# git commit -m "Add greeting feature"
# git push origin feature-greeting

# [feature-greeting 9c8dee8] Add greeting feature
#  Committer: Krishn Mukesh Navadiya <krishnmukeshnavadiya@Krishn-MacBook-Pro.local>
# Your name and email address were configured automatically based
# on your username and hostname. Please check that they are accurate.
# You can suppress this message by setting them explicitly. Run the
# following command and follow the instructions in your editor to edit
# your configuration file:

#     git config --global --edit

# After doing this, you may fix the identity used for this commit with:

#     git commit --amend --reset-author

#  1 file changed, 0 insertions(+), 0 deletions(-)
#  create mode 100644 feature.py
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 340 bytes | 340.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# remote: 
# remote: Create a pull request for 'feature-greeting' on GitHub by visiting:
# remote:      https://github.com/Krishnnavadiya/my-git-project/pull/new/feature-greeting
# remote: 
# To https://github.com/Krishnnavadiya/my-git-project.git
#  * [new branch]      feature-greeting -> feature-greeting

#  Open a Pull Request (PR)
# On GitHub:
# Go to your repo
# Click Compare & Pull Request
# Base: main
# Compare: feature-greeting
# PR title:
# “Add greeting feature”
# Description:
# “This PR adds a simple greeting function.”
# (Screenshot)

# git checkout main
# (Change main.py file)

# git add main.py
# git commit -m "Update main script message"
# git push origin main

# (Merge Conflict)
# On branch main
# Your branch is up to date with 'origin/main'.
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         gitCollobration.py
# nothing added to commit but untracked files present (use "git add" to track)
# Everything up-to-date

# (Resolve conflict)