# Introduction

In this lab, we will explore the concept of RAII in Rust, which enforces resource acquisition is initialization. This means that when objects go out of scope, their destructors are called and their owned resources are freed, eliminating the need for manual memory management and ensuring protection against resource leak bugs. We will also learn about the `Drop` trait in Rust, which allows custom destructor logic to be implemented for types that require it.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
