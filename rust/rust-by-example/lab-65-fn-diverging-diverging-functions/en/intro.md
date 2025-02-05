# Introduction

In this lab, we learn about diverging functions that are marked using `!` in Rust. Diverging functions never return and their return type is an empty type. This is different from the `()` type which has only one possible value. Diverging functions can be useful when casting to any other type is required, such as in `match` branches. They are also the return type of functions that loop forever or terminate the process.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
