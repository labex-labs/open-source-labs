```shell
git diff <branch>..<other-branch>
```

```shell
cd git-playground
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git checkout feature-1
echo "hello" >> README.md  
git add .
git commit -am "Add new content to README.md"
git checkout feature-2
echo "world" > index.html
git add .
git commit -am "Update index.html file"
git diff feature-1..feature-2
# Displays the difference between branches `feature-1` and `feature-2`
```
