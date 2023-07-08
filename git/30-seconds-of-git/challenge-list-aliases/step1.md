# List All Git Aliases

## Problem

As a developer, you may want to list all the Git aliases that have been set up on your system. This can be useful for several reasons, such as:

- Checking which aliases are available
- Finding out what commands an alias is mapped to
- Removing or modifying existing aliases

## Example

Let's say you have a Git repository named `git-playground` located at `https://github.com/labex-labs/git-playground`. You can navigate to this repository on your local machine and run the above command to list all the Git aliases that have been set up on your system.

You have set up the following aliases:
```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. Use the sed command during the listing of all of Git's aliases.

Running the command will output:
```shell
st=status
co=checkout
rb=rebase
```
