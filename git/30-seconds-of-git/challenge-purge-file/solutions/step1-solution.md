```shell
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <path>" \
  --prune-empty --tag-name-filter cat -- --all
git push --all < remote > --force
```

```shell
git filter-branch --force --index-filter  "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
# Purges `file1.txt` from history
git push origin --force --all
# Force pushes the changes to the remote repository
```
