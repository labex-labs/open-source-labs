# Solutions

```shell
git branch <branch>
git reset HEAD~1 --hard
git checkout <branch>
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
echo "hello,world" >> hello.txt
git add .
git commit -m "Added hello.txt"
git branch feature
# `feature` branch is created containing the commit "Added hello.txt"
git reset HEAD~1 --hard # Remove the commit from `master`
git log
git checkout feature
git log # Verify that the changes are now in `feature`
```
