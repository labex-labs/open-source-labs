# Introduction

In this lab, we explore operator overloading in Rust and how it can be achieved through traits. Operators in Rust can be overloaded using traits, which allows them to perform different tasks based on their input arguments. The `+` operator, for example, is syntactic sugar for the `add` method and can be used by any implementor of the `Add` trait. The traits that overload operators, including `Add`, can be found in `core::ops`. The provided Rust code demonstrates how to overload the `+` operator for custom types `Foo` and `Bar`, resulting in different output types `FooBar` and `BarFoo` respectively.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
