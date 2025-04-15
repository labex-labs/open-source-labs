# Solutions

```shell
# Picks changes from the commits `3050fc0de`, `c191f90c7` and `0b552a6d4`

# Picks changes from the commits in the range `3050fc0de` - `c191f90c7`
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b one-branch
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
git log
git checkout master
git cherry-pick 1609c283ec86ee4
git log
```
