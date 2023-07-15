```shell
git log --oneline --no-merges
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b feature1
echo "Feature 1" >> file.txt
git add .
git commit -m "Add feature 1"
git checkout master
git merge --no-ff feature1 
git log --oneline
git log --oneline --no-merges
```
