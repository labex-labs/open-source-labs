# Introduction

In this lab, we learn about variable bindings, their scope, and the concept of shadowing in Rust. Variable bindings are confined to a block, which is a collection of statements enclosed by braces. There are two examples provided to illustrate these concepts. The first example shows how a variable binding declared inside a block is limited to that block's scope and is not accessible outside of it. The second example demonstrates variable shadowing, where a new binding with the same name is declared inside a block, effectively shadowing the outer binding.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
