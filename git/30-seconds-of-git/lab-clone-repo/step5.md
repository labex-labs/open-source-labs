# Clone a Specific Branch

Sometimes, you might want to clone only a specific branch of a repository. This can be useful when you're only interested in a particular feature or version of the project.

Let's clone a specific branch of the repository:

```bash
cd ~/project
git clone -b main https://github.com/labex-labs/git-playground.git branch-repo
```

The `-b main` option tells Git to clone only the `main` branch. Replace `main` with the name of the branch you want to clone if it's different.

After cloning, navigate into the new directory and check which branch you're on:

```bash
cd branch-repo
git branch
```

You should see only the `main` branch (or whichever branch you specified).

This approach can save time and disk space when working with large repositories where you only need a specific branch.
