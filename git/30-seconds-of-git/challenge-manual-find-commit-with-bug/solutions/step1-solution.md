# Solutions

```shell
# ... some time later the bad commit will be printed
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
