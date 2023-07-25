```shell
git checkout <branch>
git rebase <base-branch>
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b one-branch
echo "hello,world" >> README.md
git add .
git commit -am "Added some changes to README.md"
git checkout master
git pull
git rebase feature-branch 
# `master` is rebased onto `feature-branch`
git log
```
