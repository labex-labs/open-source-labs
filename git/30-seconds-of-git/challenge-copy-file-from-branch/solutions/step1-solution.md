```shell
git checkout <branch> <file>
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git checkout -b feature-1
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
git checkout master
git checkout -b feature-2
git checkout feature-1 hello.txt
ll
# `feature-2` branch now contains the hello.txt file from `feature-1`
```
