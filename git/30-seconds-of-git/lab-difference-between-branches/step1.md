# Difference Between Branches

You have been working on a project with your team, and you have created a branch named `feature-1` to work on a new feature. Your colleague has also created a branch named `feature-2` to work on a different feature. You want to compare the changes between the two branches to see what has been added, modified, or deleted. How can you view the difference between the two branches?

Suppose your GitHub account clones a repository called `git-playground` from `https://github.com/labex-labs/git-playground.git`.Follow the steps below:

1. Change to the repository's directory using the command `cd git-playground`.
2. Configure your GitHub account in this environment using the commands `git config --global user.name "Your Name"` and `git config --global user.email "your@email.com"`.
3. Create and switch to the `feature-1` branch using the command `git checkout -b feature-1`, add "hello" to the `README.md` file, add it to the staging area and commit, the commit message is "Add new content to README.md" using the commands `echo "hello" >> README.md `, `git add .` and `git commit -am "Add new content to README.md"`.
4. Switch back to the `master` branch.
5. Create and switch to the `feature-2` branch using the command `git checkout -b feature-2`, add "world" to the `index.html` file, add it to the staging area and commit, the commit message is "Update index.html file" using the commands `echo "world" > index.htm`, `git add .` and `git commit -am "Update index.html file"`.
6. View the difference between the two branches using the command `git diff feature-1..feature-2`.

The output should display the difference between the `feature-1` and `feature-2` branches.This shows how the final result will look like:

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
