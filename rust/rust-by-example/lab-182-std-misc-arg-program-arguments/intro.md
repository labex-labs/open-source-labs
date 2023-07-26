# Introduction

In this lab, you can access command line arguments in Rust using the `std::env::args` function, which returns an iterator that yields a `String` for each argument. The first argument in the returned vector is the path used to call the program, while the rest of the arguments are the command line parameters. Alternatively, you can use crates like `clap` for more advanced command line argument handling.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
