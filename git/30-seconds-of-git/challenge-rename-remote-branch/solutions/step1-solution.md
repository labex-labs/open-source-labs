```shell
git branch -m <old-name> <new-name>
git push origin --delete <old-name>
git checkout <new-name>
git push origin -u <new-name>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout feature-branch
git branch -m feature-branch new-feature-1 # Renamed the local branch to `new-feature-1`
git push origin --delete feature-branch
git push origin -u new-feature-1 # Renames the remote branch to `new-feature-1`
```
