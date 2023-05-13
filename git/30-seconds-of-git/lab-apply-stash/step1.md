# Apply a stash

You are working on a feature branch in the `git-playground` repository and you need to switch to another branch to work on a bug fix. However, you have some changes that are not ready to be committed yet. You want to save these changes and switch to the other branch. Once you are done with the bug fix, you want to apply the stash and continue working on your feature branch.

1. Clone the `git-playground` repository:

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Change to the `git-playground` directory:

```
cd git-playground
```

3. Create a new branch called `feature-branch`:

```
git checkout -b feature-branch
```

4. Make some changes to the files in the repository:

```
echo "some changes" >> README.md
```

5. Save the changes to a stash:

```
git stash save "my changes"
```

6. Switch to the `master` branch:

```
git checkout master
```

7. Make some changes to the files in the repository:

```
echo "some bug fixes" >> README.md
```

8. Save the changes to a stash:

```
git stash save "some bug fixes"
```

9. Switch back to the `feature-branch`:

```
git checkout feature-branch
```

10.Add all modified and new files in your current working directory to the Git staging area.

```
git add .
```

11.View all saved stashes:

```
git stash list
```

12.Apply the stash:

```
git stash apply stash@{0}
```

13. Check the status of the repository:

```
git status
```

You should see that the changes you made before stashing are now applied.
