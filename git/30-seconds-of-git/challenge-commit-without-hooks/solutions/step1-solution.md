```shell
git commit --no-verify -m <message>
```

```shell
# Make some changes to files, ones that your precommit hook might not allow
git add .
git commit --no-verify -m "Unsafe commit"  
# Creates a commit with the message "Unsafe commit", without running git hooks
```
