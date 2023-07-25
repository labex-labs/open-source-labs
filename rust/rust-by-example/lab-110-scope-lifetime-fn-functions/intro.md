# Introduction

In this lab, we are introduced to function signatures with lifetimes in Rust, where any reference must have an annotated lifetime and any reference being returned must have the same lifetime as an input or be `static`. It is important to note that returning references without input is prohibited if it would result in returning references to invalid data. The examples provided demonstrate valid forms of functions with lifetimes, including functions with one input reference, functions with mutable references, functions with multiple elements and different lifetimes, and functions that return references that have been passed in as parameters.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
