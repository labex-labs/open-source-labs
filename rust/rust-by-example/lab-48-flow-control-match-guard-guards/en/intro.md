# Introduction

In this lab, we learn about using match guards in Rust to filter arms based on conditions. The match guard is added after the pattern and is represented by the `if` keyword followed by a condition. The guard condition allows us to further refine the matching of patterns and perform additional checks before executing the corresponding arm of the match expression. However, it is important to note that the compiler does not consider guard conditions when checking pattern coverage, so it's necessary to ensure that all patterns are still covered by the match expression.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
