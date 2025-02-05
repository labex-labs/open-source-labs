# Introduction

In this lab, we learn that a `where` clause in Rust can be used to express bounds for generic types separately from their declaration, allowing for clearer syntax, and can also apply bounds to arbitrary types rather than just type parameters. The `where` clause is especially useful when the bounds are more expressive than the normal syntax, as shown in the example involving the `PrintInOption` trait.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
