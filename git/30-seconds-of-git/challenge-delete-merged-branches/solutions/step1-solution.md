```shell
git branch --merged master | awk '!/^[ *]*$/ && !/master/ {print $1}' | xargs git branch -d
```

```shell
cd git-playground
git branch --merged
git branch --merged master | awk '!/^[ *]*$/ && !/master/ {print $1}' | xargs git branch -d
git branch
```
