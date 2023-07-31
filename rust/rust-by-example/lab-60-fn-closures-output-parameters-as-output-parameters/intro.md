# Introduction

In this lab, we learn that closures can be used as input parameters and can also be returned as output parameters by utilizing `impl Trait` and specifying the valid traits (`Fn`, `FnMut`, `FnOnce`). The `move` keyword is used to indicate that all captures occur by value, avoiding invalid references.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
