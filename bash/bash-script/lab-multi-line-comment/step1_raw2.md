# Multi-line Comment

## Introduction

Bash is a popular shell used in Linux and Unix operating systems. It provides a powerful command-line interface for users to interact with the system. In this challenge, we will explore the use of multi-line comments in Bash scripts.

## Problem

Create a Bash script that calculates the area of a rectangle. The script should prompt the user to enter the length and width of the rectangle, and then calculate and display the area. Use multi-line comments to explain the purpose of the script and any important details.

## Requirements

- The script should be named `rectangle-area.sh`.
- The script should prompt the user to enter the length and width of the rectangle.
- The script should calculate the area of the rectangle using the formula `area = length * width`.
- The script should display the calculated area to the user.
- Use multi-line comments to explain the purpose of the script and any important details.

## Solution

Create a new Bash script named `rectangle-area.sh` and add the following code:

```bash
#!/bin/bash
: '
This script calculates the area of a rectangle.
The user will be prompted to enter the length and width of the rectangle.
The area will be calculated using the formula area = length * width.
The calculated area will be displayed to the user.
'
echo "Enter the length of the rectangle: "
read length
echo "Enter the width of the rectangle: "
read width
area=$((length * width))
echo "The area of the rectangle is: $area"
```

Save the file and make it executable using the command `chmod +x rectangle-area.sh`. Then, run the script using the command `./rectangle-area.sh`.

## Summary

In this challenge, we learned how to use multi-line comments in Bash scripts to explain the purpose of the script and any important details. We also created a Bash script that calculates the area of a rectangle using user input and the formula `area = length * width`.