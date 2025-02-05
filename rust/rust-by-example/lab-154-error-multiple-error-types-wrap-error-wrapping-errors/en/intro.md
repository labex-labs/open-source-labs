# Introduction

In this lab, the alternative approach of wrapping errors in a custom error type is demonstrated. The code example showcases how to define a `Result` type alias that uses the `DoubleError` enum as the error variant, which wraps the standard library's `ParseIntError`. By implementing the `fmt::Display`, `error::Error`, and `From` traits, the custom error type can provide additional information and handle underlying errors.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
