# Introduction

In this lab, we are implementing `fmt::Display` for a structure called `List` which contains a `Vec` in Rust. The challenge is to handle each element sequentially using the `write!` macro, as it generates a `fmt::Result` which needs to be properly handled. To address this, we can use the `?` operator to check if `write!` returns an error and return it if it does, otherwise continue with the execution. By implementing `fmt::Display` for `List`, we can iterate over the elements in the vector and print them within square brackets, separated by commas. The task is to modify the program to also print the index of each element in the vector. The expected output after the modification is `[0: 1, 1: 2, 2: 3]`.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
