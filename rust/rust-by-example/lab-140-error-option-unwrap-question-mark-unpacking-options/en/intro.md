# Introduction

In this lab, we explore the use of the `?` operator in Rust, which allows for easy unpacking of `Option` values without the need for nested `match` statements. The `?` operator can be used to quickly return the underlying value if the `Option` is `Some`, or terminate the function and return `None` if the `Option` is `None`. This operator can be chained together to make code more readable and concise.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
