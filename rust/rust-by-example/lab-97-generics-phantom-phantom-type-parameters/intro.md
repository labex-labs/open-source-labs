# Introduction

In this lab, we explore the concept of phantom type parameters, which are type parameters that are checked statically at compile time and do not have any runtime behavior or values. We demonstrate their usage in Rust by combining `std::marker::PhantomData` with the concept of phantom type parameters to create tuples and structs that contain different data types.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
