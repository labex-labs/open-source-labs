# Command Substitution

You can assign a variable with the value of a command output using command substitution. Command substitution can be done by enclosing the command with \`\`(back-ticks) or `$()`.

```bash
FILELIST=$(ls)
FileWithTimeStamp=/tmp/file_$(/bin/date +%Y-%m-%d).txt

echo "FileWithTimeStamp = $FileWithTimeStamp"
echo "FILELIST = $FILELIST"
```

Note that when the script runs, it will execute the command inside the `$()` parenthesis and capture its output.

```bash
./variables.sh
```

```text
FileWithTimeStamp = /tmp/file_2023-09-01.txt
FILELIST = variables.sh
```
