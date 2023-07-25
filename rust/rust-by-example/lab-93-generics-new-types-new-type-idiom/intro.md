# Introduction

In this lab, we explore the `newtype` idiom, which provides compile-time guarantees by allowing us to create a new type that is distinct from its underlying type. An example is shown where a struct `Years` is used to represent age in years, and a struct `Days` is used to represent age in days. By using the `newtype` idiom, we can ensure that the right type of value is supplied to a program, such as in the age verification function `old_enough`, which requires a value of type `Years`. Additionally, we learn how to obtain the value of a `newtype` as its underlying type using tuple or destructuring syntax.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
