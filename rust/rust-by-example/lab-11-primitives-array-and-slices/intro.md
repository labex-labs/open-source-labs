# Introduction

In this lab, we will explore arrays and slices in Rust. An array is a collection of objects of the same type stored in contiguous memory, and its length is known at compile time. On the other hand, a slice is similar to an array but its length is not known at compile time. Slices can be used to borrow a section of an array. We will also cover how to create arrays, access elements, calculate the length, allocate memory, borrow arrays as slices, and work with empty slices. Additionally, we will discuss how to safely access array elements using `.get()` method and handle out-of-bounds errors.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
