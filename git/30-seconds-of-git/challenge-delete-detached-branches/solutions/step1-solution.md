# Solutions

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout feature-branch
git push origin --delete feature-branch
git checkout master
git branch
# feature-branch
# master
# Assuming `feature-branch` is detached
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
git branch
# master
```
