# Introduction

In this lab, we learn about bounds in Rust, which are used to restrict the lifetimes or traits of generic types. The `:` character is used to indicate that all references in a type must outlive a certain lifetime, while `+` is used to indicate that a type must implement a trait and all references in it must outlive a certain lifetime. An example code snippet demonstrates the syntax and usage of bounds in Rust.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
