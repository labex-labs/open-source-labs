# Introduction

In this lab, we will explore the concept of strings in Rust. Rust has two types of strings: `String` and `&str`.

A `String` is a heap-allocated, growable string that is guaranteed to be a valid UTF-8 sequence. On the other hand, `&str` is a slice that points to a valid UTF-8 sequence and can be used to view into a `String`.

In Rust, string literals can be written in different ways, including using escapes to represent special characters. For example, `\x3F` represents the question mark character and `\u{211D}` represents a Unicode code point. Raw string literals can also be used if you want to write a string as-is without escapes.

If you need to work with byte strings, Rust provides byte string literals using the `b` prefix. Byte strings can have byte escapes, but not Unicode escapes. Raw byte strings can also be used in a similar fashion to raw string literals.

It's important to note that `str` and `String` must always be valid UTF-8 sequences. If you need to work with strings in different encodings, you can use external crates like `encoding` for conversions between character encodings.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
