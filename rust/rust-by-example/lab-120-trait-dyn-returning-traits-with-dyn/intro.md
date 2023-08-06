# Introduction

In this lab, we learn how to workaround the limitation of returning traits directly in Rust by using the `Box<dyn Animal>` type, which allows functions to return a reference to a heap-allocated object that implements the `Animal` trait.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
