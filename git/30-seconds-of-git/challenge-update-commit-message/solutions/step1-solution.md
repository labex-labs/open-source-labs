```shell
git commit --amend -m <message>

git commit --amend -m "Fix the network bug"
# The last commit's message is now "Fix the network bug"
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git commit --amend -m "Fix the network bug"
git log --oneline
```
