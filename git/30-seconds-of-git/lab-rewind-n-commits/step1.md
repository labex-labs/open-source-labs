# Git Challenge: Rewind Commits

As a developer, you have been working on a project and have made several commits. However, you realize that the last few commits contain errors and you need to go back to a previous version of your code. You need to use Git to rewind your commits and get back to the previous version of your code.

To complete this experiment, you will use the Git repository `git-playground` from your GitHub account, which comes from a fork of `https://github.com/labex-labs/git-playground.git`.Follow these steps:

1. Clone the repository to your local machine:
```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```
2. Create a new branch called `rewind-commits`:
```shell
git checkout -b rewind-commits
```
3. Create a new file called hello.py with the text "Hello, World" and add it to the Git staging area. Then commit the changes with the message "Add hello.py file":
```shell
echo "Hello, World" > hello.py
git add hello.py
git commit -m "Add hello.py file"
```
4. Update the contents of the file hello.py to "Hello, Git" and add the changes to the Git staging area. Then use the "Update hello.py file" message to commit the changes:
```shell
echo "Hello, Git" > hello.py
git add hello.py
git commit -m "Update hello.py file"
```
5. Realize that the last few commits contain errors and you need to go back to the previous version of your code.
6. Use Git to rewind your commits by 1:
```shell
git reset HEAD~1 --hard
```
7. Verify that you have successfully rewound your commits by checking the code in your working directory.
```shell
cat hello.py

#This should output the contents of the `hello.py` file as "Hello, World", which is before the last commit is made.
```
8. Push your changes to the `rewind-commits` branch:
```shell
git push --force origin rewind-commits
```

This is the final result:

![result](./assets/challenge-rewind-n-commits-step1-1.png)