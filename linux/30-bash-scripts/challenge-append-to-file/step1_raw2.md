# Append to File

## Introduction

In this Bash challenge, we will learn how to append new data to an existing file using the '>>' operator in Bash.

## Problem

Suppose we have a file named 'book.txt' and we want to add new content to it without deleting the existing content. We can achieve this by using the '>>' operator in Bash. The problem is to create a Bash script that appends new content to the end of the 'book.txt' file.

## Requirements

- Create a Bash script named 'append_file.sh'.
- The script should display the existing content of the 'book.txt' file before appending new content.
- The script should append the text 'Learning Laravel 5' to the end of the 'book.txt' file.
- The script should display the updated content of the 'book.txt' file after appending new content.

## Solution

Here is the Bash script that appends new content to the 'book.txt' file:

```bash
#!/bin/bash

echo "Before appending the file"
cat book.txt

echo "Learning Laravel 5" >> book.txt
echo "After appending the file"
cat book.txt
```

To run the script, use the following command:

```bash
bash append_file.sh
```

## Summary

In this Bash challenge, we learned how to append new data to an existing file using the '>>' operator in Bash. We created a Bash script that appends new content to the end of the 'book.txt' file and displayed the existing and updated content of the file.
