# Introduction

In this lab, we have an example of argument parsing using pattern matching in Rust. The program takes command-line arguments and performs different operations based on the number and type of arguments passed. If no arguments are passed, it prints a message. If a single argument is passed and it can be parsed as the integer 42, it prints "This is the answer!". If a command and an integer argument are passed, it performs either an increase or decrease operation on the integer. If any other number of arguments are passed, it shows a help message explaining the correct usage of the program.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
