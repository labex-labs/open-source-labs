# Introduction

In this lab, we learn that when writing functions in Rust that take a closure as an input parameter, the closure's complete type must be annotated using one of the `traits`: `Fn`, `FnMut`, or `FnOnce`, which determine how the closure uses the captured value, either by reference, mutable reference, or value. The compiler captures variables in the least restrictive manner possible based on the chosen trait for the closure.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
