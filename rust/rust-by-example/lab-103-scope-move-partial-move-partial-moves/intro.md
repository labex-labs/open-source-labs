# Introduction

In this lab, we learn about partial moves within the destructuring of a single variable, where both `by-move` and `by-reference` pattern bindings can be used simultaneously. This results in a partial move of the variable, allowing some parts to be moved while others can still be referenced. If a parent variable is partially moved, it cannot be used as a whole afterwards, but the parts that are only referenced and not moved can still be used.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
