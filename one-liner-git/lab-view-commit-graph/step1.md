# Git Challenge: View a Visual Graph of the Repository

As a developer, you may need to view the history of a repository to understand how the code has changed over time. However, simply viewing a list of commits can be overwhelming and difficult to understand. This is where the Git graph comes in. By visualizing the history of a repository, you can quickly see how the code has evolved and identify any issues or bugs that may have been introduced.

To view a visual graph of a Git repository, you can use the `git log` command with the `--graph` option. For example, let's say you want to view the history of the `git-playground` repository on GitHub. First, you would need to clone the repository to your local machine:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

Once you have cloned the repository, you can navigate to the directory and use the `git log` command to view the graph:

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

This will display a visual graph of all the commits and branches in the repository, allowing you to see how the code has evolved over time.
