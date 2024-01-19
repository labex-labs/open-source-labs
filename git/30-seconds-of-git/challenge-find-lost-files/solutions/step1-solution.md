# Solutions

```shell
git fsck --lost-found
```

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
git checkout master
git branch -D one-branch
git fsck --lost-found
ls .git/lost-found
```
