# Solutions

```shell
git commit -m < message > --author="<name> <email>"
```

```shell
# Make some changes to files
git config --global user.email "your email"
git config --global user.name "your username"
echo "Fix the network bug" > README.md
git add .
git commit -m "Fix the network bug" --author="John Doe <john.doe@example.com>"
# Creates a commit by `John Doe`
```
