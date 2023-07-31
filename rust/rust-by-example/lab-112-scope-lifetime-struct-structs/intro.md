# Introduction

In this lab, we have some Rust code that demonstrates the usage of lifetimes in structs. The code includes a struct called `Borrowed` that holds a reference to an `i32`, and the reference must outlive the struct itself. There is also a struct called `NamedBorrowed` with two references to `i32`, both of which must outlive the struct. Additionally, there is an enum called `Either` that can either be an `i32` or a reference to one, and the reference must outlive the enum. Finally, the code creates instances of these structs and enum, and prints their contents to showcase the usage of lifetimes in Rust.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
