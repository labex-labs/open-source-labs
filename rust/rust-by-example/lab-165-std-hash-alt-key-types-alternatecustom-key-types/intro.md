# Introduction

In this lab, we explore the use of alternate/custom key types in Rust's `HashMap`, which can include types that implement the `Eq` and `Hash` traits such as `bool`, `int`, `uint`, `String`, and `&str`. Additionally, we can implement these traits for custom types by using the `#[derive(PartialEq, Eq, Hash)]` attribute, allowing them to be used as keys in a `HashMap`.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
