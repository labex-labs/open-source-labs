# Solutions

```shell
git branch --sort=-committerdate
```

```shell
git clone https://github.com/labex-labs/git-playground
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
