# Solutions

```shell
git stash apply <stash>
```

```shell
cd git-playground
git checkout master
echo "hello,world" > file1.txt
git stash save "fix the bug"
git checkout feature-branch
git stash apply stash@{1} # Applies `stash@{1}`
```
