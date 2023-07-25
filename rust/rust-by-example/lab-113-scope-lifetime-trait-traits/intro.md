# Introduction

In this lab, we explore the annotation of lifetimes in trait methods, which is similar to functions. It involves annotating lifetimes in the `impl` block as well. The provided code demonstrates an example where a struct `Borrowed` has a lifetime annotation, and the `Default` trait is implemented for it using the annotated lifetime. The main function then creates an instance of `Borrowed` using the `Default::default()` method, showcasing the usage of lifetimes in trait methods.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
