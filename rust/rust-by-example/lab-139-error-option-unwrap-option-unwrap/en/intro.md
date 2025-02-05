# Introduction

In this lab, we learn about the `Option` enum in Rust's `std` library, which is used to handle cases where absence is a possibility. It provides two options: `Some(T)` for when an element of type `T` is found, and `None` for when no element is found. These cases can be explicitly handled using `match` or implicitly handled using `unwrap`. Explicit handling allows for greater control and meaningful output, while `unwrap` can either return the inner element or induce a panic.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
