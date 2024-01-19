# Solutions

```shell
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <path>" \
  --prune-empty --tag-name-filter cat -- --all
git push --all < remote > --force
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git rm --cached --ignore-unmatch file1.txt
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
# Purges `file1.txt` from history
git push origin --force --all
# Force pushes the changes to the remote repository
```
