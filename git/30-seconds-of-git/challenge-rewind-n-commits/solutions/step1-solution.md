# Solutions

```shell
git reset [--hard] HEAD~<n>

git reset HEAD~1
# Rewinds back 1 commits but keeps changes in the working directory

git reset --hard HEAD~3
# Rewinds back 3 commits and deletes changes
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b rewind-commits
git log
git reset HEAD~1 --hard
git log
git push --force origin rewind-commits
```
