# Introduction

In this lab, we have a code snippet in Rust that demonstrates how to spawn native OS threads using the `spawn` function and a moving closure. The code creates a vector to hold the spawned threads, iterates through a range of numbers to spawn multiple threads, and prints a message identifying each thread number. Finally, the main thread waits for each spawned thread to finish using the `join` function.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
