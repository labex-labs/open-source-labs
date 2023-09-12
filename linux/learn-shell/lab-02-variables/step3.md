# Command Substitution

You can assign a variable with the value of a command output using command substitution. Command substitution can be done by enclosing the command with ``(back-ticks) or`$()`.

```bash
FILELIST=`ls`
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%d).txt
```

Note that when the script runs, it will execute the command inside the `$()` parenthesis and capture its output.
