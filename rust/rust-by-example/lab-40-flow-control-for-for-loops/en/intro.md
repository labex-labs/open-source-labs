# Introduction

In this lab, we learn about using `for` loops and ranges in Rust. We can use the `for` loop along with the `range` notation `a..b` to iterate through a range of values. For example, we can write the FizzBuzz program using a `for` loop instead of a `while` loop. Additionally, we can use the `..=` notation for a range that is inclusive on both ends. The `for` loop can also interact with iterators in different ways, such as using `iter` to borrow each element of a collection, `into_iter` to consume the collection, or `iter_mut` to mutably borrow each element of the collection. Each of these methods provides a different view of the data within the collection, allowing for different actions to be performed.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
