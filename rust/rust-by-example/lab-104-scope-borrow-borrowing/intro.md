# Introduction

In this lab, we learn about borrowing in Rust, which allows accessing data without taking ownership by using references ('&T') instead of passing objects by value ('T'). The borrow checker ensures that references always point to valid objects and prevents destruction of objects that are being borrowed.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
