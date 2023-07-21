```shell
git checkout <target-branch>
git merge --no-ff -m <message> <source-branch>
```

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b feature-branch
echo "This is a new line." >> README.md
git add .
git commit -am "Add new line to README.md"
git checkout master
git merge --no-ff -m "Merge feature-branch" feature-branch
# Merges the `feature-branch` branch into `master` and creates a commit with the message "Merge feature-branch"
``` 
