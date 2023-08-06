# Introduction

In this lab, we explore the concept of associated types in Rust, which allows for improved readability of code by defining inner types locally within a trait as output types. This is achieved by using the `type` keyword within the trait definition. With associated types, functions that use the trait no longer need to explicitly express the types `A` and `B`, making the code more concise and flexible. We rewrite an example from a previous section using associated types to illustrate their usage in practice.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
