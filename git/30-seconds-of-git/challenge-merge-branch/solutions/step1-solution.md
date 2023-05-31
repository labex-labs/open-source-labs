```shell
git checkout <target-branch>
git merge <source-branch>
```

```shell
git checkout -b feature-branch-A
echo "hello" > file2.txt
git add .
git commit -m "fix file2.txt"
git checkout master
git merge feature-branch-A # Merges the `feature-branch-A` branch into `master`
git push
git log
```
