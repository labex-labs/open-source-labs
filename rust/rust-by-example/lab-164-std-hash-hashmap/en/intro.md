# Introduction

In this lab, we learn about `HashMap` in Rust, which is used to store values by key. `HashMap` keys can be of various types, including booleans, integers, strings, or any other type that implements the `Eq` and `Hash` traits. `HashMaps` can grow and shrink dynamically based on the number of elements. We can create a `HashMap` with a specific capacity using `HashMap::with_capacity(uint)` or use `HashMap::new()` to get a `HashMap` with a default initial capacity. The provided code example demonstrates the usage of `HashMap` by storing contact names and phone numbers and performing operations like insertion, retrieval, modification, and removal.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
