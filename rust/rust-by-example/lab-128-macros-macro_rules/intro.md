# Introduction

In this lab, we will explore the powerful macro system provided by Rust, which allows for metaprogramming by expanding macros into abstract syntax trees. The `macro_rules!` macro is used to create macros, and they are distinguished from functions by their ending bang `!`. Macros are useful for avoiding code repetition, creating domain-specific languages, and defining variadic interfaces for functions that can take a variable number of arguments.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
