# Introduction

In this lab, we learn about the `panic!` macro in Rust, which can be used to generate a panic and start unwinding its stack, causing the program to report the panic message and exit. The runtime takes care of freeing all the resources owned by the thread by calling the destructor of its objects. We also look at an example of using the `panic!` macro to handle division by zero and verify that it doesn't result in memory leaks using Valgrind.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
