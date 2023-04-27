```shell
git bisect start
git bisect good <commit>
git bisect bad <commit>
git bisect (bad | good)
git bisect reset [<commit>]
```

```shell
git bisect start
git bisect good 3050fc0de
git bisect bad c191f90c7
git bisect good # Current commit is good
git bisect bad  # Current commit is buggy
# ... some time later the bad commit will be printed
git bisect reset # Goes to the original branch
```
