# Introduction

In this lab, you can use `cargo doc` to build documentation in `target/doc`. You can also use `cargo test` to run all tests, including documentation tests, and `cargo test --doc` to only run documentation tests. Doc comments, denoted by `///`, are compiled into documentation by `rustdoc` and support Markdown. These comments are useful for documenting code in big projects. Doc attributes, such as `inline`, `no_inline`, and `hidden`, are frequently used with `rustdoc`. Rustdoc is widely used by the community for generating documentation, including the standard library docs.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
