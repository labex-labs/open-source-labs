# Introduction

In this lab, we will explore the `Path` struct in Rust, which represents file paths in the underlying filesystem. It comes in two flavors: `posix::Path` for UNIX-like systems and `windows::Path` for Windows. The `Path` can be created from an `OsStr` and provides various methods to retrieve information from the file or directory that the path points to. It is important to note that a `Path` is immutable, and its owned version is called `PathBuf`, which can be mutated in-place. The relation between `Path` and `PathBuf` is similar to that between `str` and `String`.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
