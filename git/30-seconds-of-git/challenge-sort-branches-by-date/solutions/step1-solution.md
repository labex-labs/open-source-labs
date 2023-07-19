```shell
git branch --sort=-committerdate
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b one
touch hello.txt
git add .
git commit -m "hello.txt"
git checkout master
git checkout -b two
git branch --sort=-committerdate
```
