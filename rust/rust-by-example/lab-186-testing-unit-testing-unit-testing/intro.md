# Introduction

In this lab, we learn about unit testing in Rust. Unit tests are Rust functions that verify the non-test code by performing setup, running the code, and asserting the results. These tests are written in a `tests` mod with the `#[cfg(test)]` attribute and marked with the `#[test]` attribute. Tests can fail if something in the test function panics, and helper macros like `assert!`, `assert_eq!`, and `assert_ne!` are used for assertions. Rust 2018 allows unit tests to return `Result<()>` to use the `?` operator for concise testing. There is also support for testing panics using the `#[should_panic]` attribute. Specific tests can be run using the test name with the `cargo test` command, and tests can be ignored using the `#[ignore]` attribute or by running `cargo test -- --ignored`.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
