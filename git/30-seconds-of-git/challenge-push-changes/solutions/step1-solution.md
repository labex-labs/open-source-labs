```shell
git push
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
echo "hello,world" >> file1.txt
git add .
git commit -m "Added new feature"
git push origin master # The remote `master` branch is now up to date with the local branch
```
