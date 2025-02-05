# Introduction

In this lab, you will learn about the `cfg` attribute and `cfg!` macro in Rust, which allow for conditional checks in configuration and evaluation, respectively. The `cfg` attribute enables conditional compilation, while the `cfg!` macro evaluates to true or false at run-time. Code blocks using `cfg!` must be valid regardless of the evaluation result, unlike `#[cfg]` which can remove code.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
