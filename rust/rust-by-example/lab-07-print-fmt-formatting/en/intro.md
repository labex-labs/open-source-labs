# Introduction

In this lab, we learned about formatting in Rust and how to use the `format!` macro to format variables. We saw that formatting is specified using a format string, and different argument types can be used to format the same variable in different ways. The most common formatting trait is `Display`, which handles cases where the argument type is left unspecified. We saw an example of implementing the `Display` trait for a `City` struct, where we formatted the latitude and longitude values. We also saw an example of a `Color` struct and were tasked with implementing the `Display` trait for it to display the RGB values and their hexadecimal representation.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
