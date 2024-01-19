# Solutions

```shell
git bisect start
git bisect good <commit>
git bisect bad <commit>
git bisect (bad | good)
git bisect reset [<commit>]

git bisect start
git bisect good # Current commit is good
git bisect bad  # Current commit is buggy
# ... some time later the bad commit will be printed
git bisect reset # Goes to the original branch
```

```shell
cd git-playground
git bisect start
git bisect bad HEAD
git bisect good b00b937 # This is a hash of the commit message "Initial commit"
cat file2.txt
git bisect good
git bisect reset
```
