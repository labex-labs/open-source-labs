# Introduction

In this lab, the primary way of documenting a Rust project is through annotating the source code with documentation comments, which are written in CommonMark Markdown specification and support code blocks in them. Rust takes care of correctness and these code blocks are compiled and used as documentation tests. These tests are automatically run when using the `cargo test` command. The motivation behind documentation tests is to serve as examples that exercise the functionality and allow using examples from the documentation as complete code snippets.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
