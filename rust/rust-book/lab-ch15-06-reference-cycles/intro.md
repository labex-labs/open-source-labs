# Introduction

Welcome to Reference Cycles Can Leak Memory. This lab is a part of the [Rust Book](https://doc.rust-lang.org/book/). You can practice your Rust skills in LabEx.

In this lab, we explore how Rust's memory safety guarantees make it difficult but not impossible to accidentally create memory leaks, specifically when using `Rc<T>` and `RefCell<T>` which can result in reference cycles that prevent values from being dropped and thus leaking memory.
