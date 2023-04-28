# Add Files to the Staging Area

You have been working on a project stored in a Git repository named `https://github.com/labex-labs/git-playground`. You have made some changes to the codebase and want to commit these changes to the repository. However, you only want to commit specific changes and not all the changes you have made. To do this, you need to add the files to the staging area.

Suppose you have made changes to the `index.html` and `style.css` files in the `src` directory of the `git-playground` repository. To add these files to the staging area, you can use the following command:

```shell
git add src/index.html src/style.css
```

Alternatively, you can use a fileglob to add all files with a `.js` extension in the `src` directory:

```shell
git add src/*.js
```

You can also add all changes to the staging area using the following command:

```shell
git add .
```
