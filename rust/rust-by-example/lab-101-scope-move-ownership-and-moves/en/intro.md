# Introduction

In this lab, it is explained that in Rust, variables have ownership of resources and can only have one owner, which prevents resources from being freed multiple times. When variables are assigned or function arguments are passed by value, the ownership of resources is transferred, known as a move. After the move, the previous owner can no longer be used to avoid creating dangling pointers. The code example demonstrates these concepts by showing how the ownership of stack-allocated and heap-allocated variables is transferred and how accessing a variable after its ownership has been moved leads to errors.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
