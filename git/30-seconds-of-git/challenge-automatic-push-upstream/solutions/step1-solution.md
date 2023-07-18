```shell
git config [--global] --add --bool
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git config --add --bool remote.origin.pushdefault true
git checkout -b new-feature
echo "hello,world" >> hello.txt
git add .
git commit -m "Added hello.txt"
git push --set-upstream origin new-feature
```
