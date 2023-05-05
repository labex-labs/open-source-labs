# Get User Input

## Introduction

Bash is a popular shell used in Linux and Unix-based operating systems. It provides a powerful command-line interface for users to interact with the system. In this challenge, we will focus on how to get user input using the 'read' command in Bash.

## Problem

Create a Bash script named 'user_input.sh' that takes input from the user and displays it on the screen. The script should prompt the user to enter their name and then display a welcome message that includes their name.

## Requirements

- The script should use the 'read' command to take input from the user.
- The script should prompt the user to enter their name.
- The script should display a welcome message that includes the user's name.
- The script should be named 'user_input.sh'.

## Solution

Here is an example script that meets the requirements:

```bash
#!/bin/bash
echo "Enter Your Name"
read name
echo "Welcome $name to LinuxHint"
```

Save this script as 'user_input.sh' and run it with the following command:

```bash
bash user_input.sh
```

When you run the script, it will prompt you to enter your name. After you enter your name, it will display a welcome message that includes your name.

## Summary

In this challenge, we learned how to get user input using the 'read' command in Bash. We created a script that prompts the user to enter their name and displays a welcome message that includes their name. Bash provides a powerful command-line interface for users to interact with the system, and the 'read' command is a useful tool for getting input from users.
