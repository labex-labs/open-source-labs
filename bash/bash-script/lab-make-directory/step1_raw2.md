# Make Directory

## Introduction

This challenge aims to test your knowledge of Bash commands and your ability to write a Bash script. In this challenge, you will create a Bash script that creates a new directory.

## Problem

Create a Bash script named `make_directory.sh` that takes a new directory name from the user. If the directory name does not exist in the current location, the script should create the directory. Otherwise, the script should display an error message.

## Requirements

- The Bash script should be named `make_directory.sh`.
- The script should take a new directory name from the user.
- If the directory name does not exist in the current location, the script should create the directory.
- If the directory name already exists in the current location, the script should display an error message.

## Solution

```bash
#!/bin/bash  
echo "Enter directory name"  
read newdir  
if [ ! -d "$newdir" ]; then
    mkdir "$newdir"
    echo "Directory created successfully"
else
    echo "Error: Directory already exists"
fi
```

Save the above code in a file named `make_directory.sh`. Run the script with the following command:

```bash
bash make_directory.sh
```

## Summary

In this challenge, you have learned how to create a new directory using the `mkdir` command in Bash. You have also learned how to write a Bash script that takes user input and performs conditional checks to create a new directory or display an error message.