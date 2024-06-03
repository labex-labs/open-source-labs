# Introduction

In this lab, the concept of boxing, stack allocation, and heap allocation in Rust is explored. All values in Rust are stack allocated by default, but they can be boxed (allocated on the heap) using the `Box<T>` type. A box is a smart pointer to a heap-allocated value, and when it goes out of scope, its destructor is called and the memory on the heap is freed. Boxing allows for the creation of double indirection and can be dereferenced using the `*` operator. The lab provides code examples and explanations of how boxing works and how it affects memory allocation on the stack.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
