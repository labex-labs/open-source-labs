# Wait Command

## Problem

The **wait** command is a built-in command in Linux that waits for a process to complete. It is often used in shell scripts to ensure that a process has finished before continuing with the next step. The problem is to create a Bash script that demonstrates the use of the **wait** command.

## Requirements

To complete this challenge, you need to create a Bash script named **wait_example.sh** that does the following:

- Prints a message "Wait command" to the console.
- Runs a process in the background using the "&" operator.
- Stores the process ID of the background process in a variable named "process_id".
- Waits for the process to complete using the **wait** command and the process ID.
- Prints the exit status of the process to the console.

## Example

To run the script, use the following command:

```bash
bash wait_example.sh
```

Output:

```bash
Wait command
Exited with status 0
```
