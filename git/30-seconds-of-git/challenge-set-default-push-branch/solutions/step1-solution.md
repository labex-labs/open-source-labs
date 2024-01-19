# Solutions

```shell
git config [--global] push.default current

git config --global push.default current

git checkout -b my-branch
git push -u
# Pushes to origin/my-branch
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git config push.default current
git checkout -b my-branch
echo "Hello, World" > hello.txt
git add hello.txt
git commit -m "Add hello.txt"
git push -u
```
