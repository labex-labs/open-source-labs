```shell
git commit --fixup <commit>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git log --oneline
echo "hello,world" > hello.txt
git add .
git commit --fixup cf80005
# This is the hash of the commit message "Added file1.txt".
git rebase --interactive --autosquash HEAD~3
# Now the fixup commit has been squashed
```
