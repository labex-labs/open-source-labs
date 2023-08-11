# Use of Echo Command

Create a Bash script that demonstrates the use of the `echo` command with various options. The script should print text with and without a newline, and remove backslash characters from the output.

- The Bash script should be named `echo_example.sh`.
- The script should use the `echo` command with the following options:
  - Without any option (default behavior)
  - `-n` option to print text without a newline
  - `-e` option to remove backslash characters from the output
- The script should print the following text:
  - "Printing text with newline"
  - "Printing text without newline"
  - "Removing backslash characters"
- The script should be executable.

Create a new file named `echo_example.sh` and add the following script:

```bash
#!/bin/bash
echo "Printing text with newline"
echo -n "Printing text without newline"
echo -e "\nRemoving \t backslash \t characters\n"
```

Save the file and make it executable using the following command:

```bash
chmod +x echo_example.sh
```

Run the script using the following command:

```bash
./echo_example.sh
```

The output should be:

```bash
Printing text with newline
Printing text without newlineRemoving backslash characters
```
