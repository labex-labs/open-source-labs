# List All Git Aliases

As a developer, you may want to list all the Git aliases that have been set up on your system. This can be useful for several reasons, such as:

- Checking which aliases are available
- Finding out what commands an alias is mapped to
- Removing or modifying existing aliases

To list all Git aliases, you can use the following command:

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Let's say you have a Git repository named `git-playground` located at `https://github.com/labex-labs/git-playground`. You can navigate to this repository on your local machine and run the above command to list all the Git aliases that have been set up on your system.

For example, if you have the following aliases set up:

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

Running the command will output:

```shell
st=status
co=checkout
rb=rebase
```
