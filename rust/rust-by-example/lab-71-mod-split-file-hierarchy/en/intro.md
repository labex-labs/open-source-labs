# Introduction

In this lab, the file hierarchy of the modules in the code example can be represented as follows: There is a directory named "my" which contains two files, "inaccessible.rs" and "nested.rs". Additionally, there is a file named "my.rs" and a file named "split.rs". The "split.rs" file includes the module "my" which is defined in the "my.rs" file, and the "my.rs" file includes the modules "inaccessible" and "nested" which are defined in the "inaccessible.rs" and "nested.rs" files respectively.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
