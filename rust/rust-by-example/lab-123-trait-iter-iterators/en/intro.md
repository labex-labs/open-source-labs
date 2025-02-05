# Introduction

In this lab, we learn about the `Iterator` trait in Rust, which is used to implement iterators over collections such as arrays. The `Iterator` trait requires the `next` method to be defined for the iterator, and can be manually implemented in an `impl` block or automatically defined for arrays and ranges. The `for` construct can be used to conveniently turn some collections into iterators using the `.into_iter()` method. The lab provides an example implementation of the `Fibonacci` sequence generator as an iterator, showcasing how to define the `next` method and use the `Iterator` trait. Additionally, it demonstrates the use of `take` and `skip` methods to manipulate iterators, as well as the `iter` method for iterating over arrays.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
