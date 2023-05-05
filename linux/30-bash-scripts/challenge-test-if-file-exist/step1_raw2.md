# Test if File Exist

## Introduction

In Bash, you can check the existence of a file using various options. This challenge focuses on using the '-f' option to test the file existence.

## Problem

Create a Bash script named 'file_exist.sh' that takes a filename as an argument and checks if the file exists in the current location. If the file exists, the script should print "File exists" and if the file does not exist, the script should print "File does not exist".

## Requirements

- The script should be named 'file_exist.sh'.
- The script should take a filename as an argument.
- The script should use the '-f' option to check the file existence.
- If the file exists, the script should print "File exists".
- If the file does not exist, the script should print "File does not exist".

## Solution

```bash
#!/bin/bash
filename=$1
if [ -f "$filename" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi
```

Save the above code in a file named 'file_exist.sh'. Run the following commands to check the existence of the file. Here, **book.txt** file exists and  **book2.txt** is not exist in the current location.

```bash
ls
bash file_exist.sh book.txt
bash file_exist.sh book2.txt
```

## Summary

In this challenge, we learned how to check the existence of a file in Bash using the '-f' option. We created a Bash script that takes a filename as an argument and checks if the file exists in the current location. If the file exists, the script prints "File exists" and if the file does not exist, the script prints "File does not exist".
