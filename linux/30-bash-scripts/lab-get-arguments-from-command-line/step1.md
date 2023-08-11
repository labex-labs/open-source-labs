# Get Arguments from Command Line

Create a Bash script named "command_line.sh" that reads two command line arguments and prints the total number of arguments and the argument values as output.

- The script should be named "command_line.sh".
- The script should read two command line arguments using the variables $1 and $2.
- The script should print the total number of arguments and the argument values as output.
- The script should be executable using the bash command.

```bash
#!/bin/bash
echo "Total arguments : $#"
echo "1st Argument = $1"
echo "2nd argument = $2"
```

Save the script as "command_line.sh" and run it using the bash command.

```bash
bash command_line.sh Linux Hint
```

The output should be:

```bash
Total arguments : 2
1st Argument = Linux
2nd argument = Hint
```
