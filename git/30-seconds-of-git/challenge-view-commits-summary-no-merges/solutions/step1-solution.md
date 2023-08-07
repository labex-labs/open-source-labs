```shell
git log --oneline --no-merges
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b feature1
echo "feature 1" >> file.txt
git add .
git commit -m "Add feature 1"
git checkout master
git merge --no-ff feature1
git log --oneline
git log --oneline --no-merges
```
