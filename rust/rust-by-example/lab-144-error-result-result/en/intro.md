# Introduction

In this lab, we will explore the `Result` type in Rust, which provides a way to handle potential errors instead of possible absence of a value like the `Option` type. The `Result` type can have two outcomes - `Ok(T)` for a successful result with element `T`, and `Err(E)` for an error with element `E`. We will see how to use `Result` in code examples and how it can be used as the return type of the `main` function to handle errors and provide a more specific error message.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
