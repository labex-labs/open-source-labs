# Solutions

```shell
git config [--global] --add merge.ff false

git config --global --add merge.ff false
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b my-branch
echo "hello,world" > hello.txt
git add .
git commit -m "Added hello.txt"
git config --global --add merge.ff false
git checkout master
git merge my-branch
# Will never fast forward even if it's possible
```
