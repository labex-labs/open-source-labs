# Use of Echo Command

## Problem

Create a Bash script that demonstrates the use of the `echo` command with various options. The script should print text with and without a newline, and remove backslash characters from the output.

## Requirements

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

## Example

To run the script, use the following command:

```bash
./echo_example.sh
```

Output:

```bash
Printing text with newline
Printing text without newline
Removing   backslash   characters
```
