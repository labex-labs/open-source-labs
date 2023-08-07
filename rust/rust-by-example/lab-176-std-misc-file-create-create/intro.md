# Introduction

In this lab, we have a `create` function that opens a file in write-only mode. It either creates a new file or destroys the old content if the file already exists. The function uses Rust's standard library to handle file operations. The example provided demonstrates how to use the `create` function to write the contents of a static `LOREM_IPSUM` string to a file named "lorem_ipsum.txt". The output shows a successful write operation confirmation, and the contents of the file are displayed using the `cat` command.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
