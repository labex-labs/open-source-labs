# Add Files to the Staging Area

You have been working on a project stored in a Git repository named `https://github.com/labex-labs/git-playground`. You have made some changes to the codebase and want to commit these changes to the repository. However, you only want to commit specific changes and not all the changes you have made. To do this, you need to add the files to the staging area.

1. You will make some changes in the `git-playground` directory:
```shell
echo "hello" > index.html 
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```
2. Add these files to the staging area:
```shell
git add index.html style.css
```
3. View the status of the current working directory and staging area, including information on which files have been modified, which files have been added to the staging area, etc:
```shell
git status
```
4. Alternatively, you can use a fileglob to add all files with a `.js` extension:
```shell
git add src/*.js
```
5. View the status of the current working directory and staging area again:
```shell
git status
```
6. You can also add all changes to the staging area:
```shell
git add .
```
7. View the status of the current working directory and staging area again:
```shell
git status
```

This is the finished result:

![<result>](./assets/challenge-stage-files-step1-1.png)
