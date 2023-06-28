```shell
git config --global core.editor <editor-command>

git config --global core.editor "vim"
# Sets vim as the git text editor
```

```shell
# Fork from https://github.com/labex-labs/git-playground.git
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
git config --global core.editor "vim"
echo "Hello, Git" > hello.txt
git add hello.txt
git commit
```
