# Introduction

In this lab, we explore the concepts of `From` and `Into` traits in Rust, which are used for converting between different types. These traits are inherently linked, with `Into` being the reciprocal of `From`. The `From` trait allows a type to define how to create itself from another type, enabling easy conversion between types. The `Into` trait automatically calls the `From` implementation when necessary. Both traits can be implemented for custom types, providing flexibility in type conversions.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
