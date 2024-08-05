# Clone to a Specific Directory

Sometimes, you might want to clone a repository into a directory with a different name. This is useful when working on multiple versions of a project or when you want to give the directory a more descriptive name.

Let's clone the same repository again, but this time into a directory named `my-project`:

```bash
cd ~/project
git clone https://github.com/labex-labs/git-playground.git my-project
```

This command does two things:

1. It clones the `git-playground` repository
2. It puts the cloned files into a new directory called `my-project` instead of `git-playground`

After the cloning process is complete, you should see output similar to this:

![<result>](./assets/challenge-clone-repo-step1-2.png)

This feature is particularly useful when:

- You already have a directory with the same name as the repository
- You want to clone the same repository multiple times for different purposes
- You want to give the directory a name that's more meaningful in the context of your local project structure

Remember, the name of the directory doesn't affect the Git repository itself - it's just the name of the folder on your local machine.
