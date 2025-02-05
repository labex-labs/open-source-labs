# Introduction

In this lab, we will explore the concept of lifetimes in Rust and how they are used by the compiler to ensure the validity of borrows in the code. Lifetimes are a construct of the compiler that determine the duration of a variable, from its creation to its destruction. While lifetimes and scopes are related, they are not the same. When borrowing a variable using the `&` operator, the borrow has a lifetime that is determined by its declaration, and it is valid as long as it ends before the lender is destroyed. However, the scope of the borrow is determined by where the reference is used. The provided example code demonstrates how lifetimes and scopes are used in practice, with each variable having its own lifetime and scope.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
