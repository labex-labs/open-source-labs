# Output Process Substitution

Process substitution can be used to chain the output of commands together. This is useful when you have commands that take a file as an argument but you want to process the output of other commands instead.

For example, if you want to compare the content of two files, you can use process substitution to avoid false positives when the lines are not ordered. Instead of creating two sorted files and comparing them, you can do it in one line.

```shell
diff <(sort file1) <(sort file2)
```

In this example, the output of the `sort` command for `file1` and `file2` is passed as arguments to the `diff` command. This allows you to compare the sorted content of the files without creating additional files.
