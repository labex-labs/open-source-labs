# Solutions

```shell
git branch --no-contains <commit>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
git log
git branch --no-contains 31c5ac20129151af1
# "31c5ac20129151af1" is the hash of the commit message "Create a new-branch branch".
```
