# List All Git Aliases

As a developer, you may want to list all the Git aliases that have been set up on your system. This can be useful for several reasons, such as:

- Checking which aliases are available
- Finding out what commands an alias is mapped to
- Removing or modifying existing aliases

Let's say you have a Git repository named `git-playground` located at `https://github.com/labex-labs/git-playground`. 

1. Navigate to this repository on your local machine:
```shell
cd git-playground
```
2. Set up the following aliases:
```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```
3. Use the `sed` command during the listing of all of Git's aliases:
```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Running the command will output:
```shell
st=status
co=checkout
rb=rebase
```
