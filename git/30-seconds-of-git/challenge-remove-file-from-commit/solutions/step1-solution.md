```shell
git rm —-cached <file>
git commit —-amend
```

```shell
Fork from `https://github.com/labex-labs/git-playground.git`
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
touch git-playground.txt
echo "hello,world" > file1.txt
git add .
git commit -m "add git-playground.txt"
git rm --cached "file1.txt"
git status
git commit --amend
# Removes `file1.txt` from the last commit
```
