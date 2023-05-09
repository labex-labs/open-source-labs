# Get Arguments from Command Line with Names

## Introduction

In Bash scripting, it is common to pass arguments to a script through the command line. However, sometimes it is useful to give names to these arguments to make the script more readable and easier to use. This challenge will show you how to read command line arguments with names in Bash.

## Problem

Create a Bash script named `command_line_names.sh` that reads two arguments, `X` and `Y`, from the command line and prints their sum. The script should be able to handle arguments passed in any order and should gracefully handle any errors or missing arguments.

## Requirements

- The script must be named `command_line_names.sh`.
- The script must read two arguments, `X` and `Y`, from the command line.
- The script must be able to handle arguments passed in any order.
- The script must gracefully handle any errors or missing arguments.
- The script must print the sum of `X` and `Y`.

## Solution

```bash
#!/bin/bash
for arg in "$@"; do
  index=$(echo $arg | cut -f1 -d=)
  val=$(echo $arg | cut -f2 -d=)
  case $index in
    X) x=$val ;;
    Y) y=$val ;;
    *) ;;
  esac
done
((result = x + y))
echo "X+Y=$result"
```

To run the script, use the following command with two command line arguments:

```bash
bash command_line_names.sh X=45 Y=30
```

## Summary

In this Bash challenge, we learned how to read command line arguments with names in Bash. By using the `case` statement and the `cut` command, we were able to parse the arguments and perform the desired operation. This technique can be useful in many situations where command line arguments need to be named for clarity and ease of use.
