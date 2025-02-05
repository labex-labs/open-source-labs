# Introduction

In this lab, we are given a naive implementation and a more efficient implementation for reading lines from a file in Rust. The naive approach uses `read_to_string` to read the file into a single string and then splits it into lines, while the more efficient approach uses a `BufReader` to read the file line by line without loading the entire contents into memory.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
