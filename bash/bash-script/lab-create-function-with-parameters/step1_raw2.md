# Create Function with Parameters

## Introduction

Bash is a powerful scripting language that allows you to automate tasks on your Linux system. In this challenge, you will learn how to create a function with parameters in Bash.

## Problem

Bash does not allow you to declare function parameters or arguments at the time of function declaration. However, you can use parameters in a function by using other variables. In this challenge, you will create a Bash script that defines a function that calculates the area of a rectangle based on the parameter values.

## Requirements

To complete this challenge, you will need to create a Bash script named `function_parameter.sh` with the following code:

```bash
#!/bin/bash

Rectangle_Area() {
    area=$(($1 * $2))
    echo "Area is : $area"
}

Rectangle_Area 10 20
```

When you run the script with the `bash` command, it should output the following:

```bash
Area is : 200
```

## Solution

To create a function with parameters in Bash, you need to define the function and then use variables to read the parameter values. In the code above, we defined a function named `Rectangle_Area` that takes two parameters. We then used the variables `$1` and `$2` to read the parameter values and calculate the area of the rectangle.

## Summary

In this challenge, you learned how to create a function with parameters in Bash. By using variables to read parameter values, you can create powerful scripts that automate tasks on your Linux system.