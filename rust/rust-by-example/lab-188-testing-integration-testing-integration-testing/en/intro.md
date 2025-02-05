# Introduction

In this lab, integration testing is discussed, which involves testing multiple parts of a library together using its public interface. Integration tests can be placed in the `tests` directory next to the `src` directory in a Rust crate, and are executed using the `cargo test` command. Additionally, common code can be shared between integration tests by creating a module with public functions and importing it within the tests.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
