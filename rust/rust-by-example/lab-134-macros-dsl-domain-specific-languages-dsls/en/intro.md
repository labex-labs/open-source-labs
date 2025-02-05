# Introduction

In this lab, we explore the concept of Domain Specific Languages (DSLs) in Rust, which are mini "languages" embedded in Rust macros. These macros expand into normal Rust constructs but offer a concise and intuitive syntax for specific functionality. A practical example is demonstrated using a calculator API, where an expression is supplied to the macro, and the output is printed to the console. This allows for the creation of more complex interfaces like the ones found in libraries such as `lazy_static` or `clap`.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
