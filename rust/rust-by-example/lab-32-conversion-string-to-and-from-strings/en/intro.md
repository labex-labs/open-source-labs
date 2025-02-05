# Introduction

In this lab, we will learn about converting to and from strings in Rust. To convert any type to a string, we can implement the `ToString` trait for the type. Alternatively, we can implement the `fmt::Display` trait, which automatically provides the `ToString` trait and allows us to print the type using `println!`. On the other hand, to parse a string into a specific type, such as a number, we can use the `parse` function along with type inference or by specifying the type using the 'turbofish' syntax. This relies on the `FromStr` trait, which is implemented for many types in the standard library. If we want to parse a string into a user-defined type, we can implement the `FromStr` trait for that type.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
