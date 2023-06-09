# Add Files to the Staging Area

## Problem

You have been working on a project stored in a Git repository named `https://github.com/labex-labs/git-playground`. You have made some changes to the codebase and want to commit these changes to the repository. However, you only want to commit specific changes and not all the changes you have made. To do this, you need to add the files to the staging area.

## Example

1. View all files in the current directory.
2. Suppose you have made changes to the `index.html` and `style.css` files in the `git-playground` directory of the `git-playground` repository. Add these files to the staging area.
3. View the status of the current working directory and staging area, including information on which files have been modified, which files have been added to the staging area, etc.
4. Alternatively, you can use a fileglob to add all files with a `.js` extension in the `src` directory.
5. View the status of the current working directory and staging area again.
6. You can also add all changes to the staging area.
7. View the status of the current working directory and staging area again.

This is the finished result:

![<result>](./assets/challenge-stage-files-step1-1.png)



1. Suppose you have made changes to the `index.html` and `style.css` files in the `git-playground` directory of the `git-playground` repository. To add these files to the staging area, you can use the following command:
```shell
git add index.html style.css
```
2. View the status of the current working directory and staging area, including information on which files have been modified, which files have been added to the staging area, etc.
3. Alternatively, you can use a fileglob to add all files with a `.js` extension in the `src` directory:
```shell
git add *.js
```
4. View the status of the current working directory and staging area again.
5. You can also add all changes to the staging area using the following command:
```shell
git add .
```
6. View the status of the current working directory and staging area again.




