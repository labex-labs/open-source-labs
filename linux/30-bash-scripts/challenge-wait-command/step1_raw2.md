# Wait Command

## Introduction

Bash is a popular shell used in Linux and Unix operating systems. It provides a command-line interface for users to interact with the system. In this challenge, we will explore the **wait** command in Bash.

## Problem

The **wait** command is a built-in command in Linux that waits for a process to complete. It is often used in shell scripts to ensure that a process has finished before continuing with the next step. The problem is to create a Bash script that demonstrates the use of the **wait** command.

## Requirements

To complete this challenge, you need to create a Bash script named **wait_example.sh** that does the following:

- Prints a message "Wait command" to the console.
- Runs a process in the background using the "&" operator.
- Stores the process ID of the background process in a variable named "process_id".
- Waits for the process to complete using the **wait** command and the process ID.
- Prints the exit status of the process to the console.

## Solution

Here is an example script that demonstrates the use of the **wait** command:

```bash
#!/bin/bash
echo "Wait command" &
process_id=$!
wait $process_id
echo "Exited with status $?"
```

To run the script, save it as **wait_example.sh** and execute the following command in the terminal:

```bash
bash wait_example.sh
```

The script will print "Wait command" to the console, run a process in the background, wait for the process to complete, and print the exit status of the process.

## Summary

The **wait** command is a useful tool in Bash for waiting for a process to complete before continuing with the next step. By using the **wait** command, you can ensure that your scripts run smoothly and without errors. In this challenge, we have created a Bash script that demonstrates the use of the **wait** command.
