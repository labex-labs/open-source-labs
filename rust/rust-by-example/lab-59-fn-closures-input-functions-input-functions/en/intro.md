# Introduction

In this lab, you will learn how functions can take closures as parameters, allowing any function that satisfies the trait bound of the closure to be used as an argument. The `Fn`, `FnMut`, and `FnOnce` traits dictate how a closure captures variables from the enclosing scope.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
