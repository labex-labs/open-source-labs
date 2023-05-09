# Use of Comment in Bash Scripting

## Introduction

In Bash scripting, comments are used to add notes or explanations to the code. These comments are ignored by the interpreter and are only meant for human readers.

## Problem

The problem is to understand how to use comments in Bash scripting.

## Requirements

To add comments in Bash scripting, use the `#` symbol at the beginning of the line. The comment can be a single line or multiple lines. It is recommended to use comments to explain the purpose of the code, add notes, or provide instructions.

## Solution

To demonstrate the use of comments, create a new file named `comment_example.sh` and add the following script with a single-line comment:

```bash
#!/bin/bash

# Add two numeric values
((sum = 25 + 35))

# Print the result
echo $sum
```

Save the file and run it with the `bash` command:

```bash
bash comment_example.sh
```

The output will be:

```bash
60
```

## Summary

In Bash scripting, comments are used to add notes or explanations to the code. They are ignored by the interpreter and are only meant for human readers. To add comments, use the `#` symbol at the beginning of the line. It is recommended to use comments to explain the purpose of the code, add notes, or provide instructions.
