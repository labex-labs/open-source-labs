```shell
git commit --amend --author="<name> <email>"
```

```shell
# Make some changes to files
git config user.email "your email"
git config user.name "your username"
echo "Hello, World" > hello.txt
git add hello.txt
git commit -m "Initial commit"
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
# The last commit's author is now `Duck Quackers`
```
