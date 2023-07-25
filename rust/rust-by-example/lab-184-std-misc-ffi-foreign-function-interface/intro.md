# Introduction

In this lab, we learn about Rust's Foreign Function Interface (FFI) that allows interaction with C libraries by declaring foreign functions within an `extern` block and annotating them with a `#[link]` attribute containing the name of the foreign library. The code example demonstrates the usage of FFI to call external functions from the `libm` library, such as computing the square root of a single precision complex number and calculating the cosine of a complex number. Safe wrappers are commonly used around these unsafe foreign function calls. The lab also includes a minimal implementation of single precision complex numbers and demonstrates how to call safe APIs wrapped around unsafe operations.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
