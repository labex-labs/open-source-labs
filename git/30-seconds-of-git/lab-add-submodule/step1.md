# Add a Submodule

Your task is to add a new submodule to a Git repository. You will need to use the `git submodule add` command to add the submodule from an upstream repository to a local directory in your repository. The syntax for the command is as follows:

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` is the URL or path to the upstream repository that you want to add as a submodule.
- `<local-path>` is the path where you want to store the submodule in your local repository.

Suppose you have a Git repository named `my-project` and you want to add a submodule from the Git repository `https://github.com/labex-labs/git-playground.git` to a directory named `git-playground` in your local repository. Here's how you can do it:

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git ./git-playground
```

This is the result after completing the lab:

![Git submodule add result](./assets/challenge-add-submodule-step1-1.png)
