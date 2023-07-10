# List All Stashes

You are working on a project in a Git repository and have made some changes that are not yet ready to be committed. You decide to stash these changes so that you can work on a different task. Later, you want to see a list of all the stashes you have created so that you can decide which one to apply. How do you list all stashes in a Git repository?

1. Navigate to the `git-playground` directory:
```
cd git-playground
```
2. Create a new file named `test.txt` and add some content to it:
```
echo "hello,world" > test.txt
git add .
```
3. Use the following command to stash your changes:
```
git stash save "Added test.txt"
```
4. Create another new file named `test2.txt` and add some content to it:
```
echo "hello,labex" > test2.txt
git add .
```
5. Use the following command to stash your changes:
```
git stash save "Added test2.txt"
```
6. Use the following command to list all stashes:
```
git stash list
```

You should see output similar to the following:
```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
