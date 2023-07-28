# Introduction

In this lab, the `open` function is introduced as a way to open a file in read-only mode by providing a path to the desired file. The function returns a `File` object that owns the file descriptor and takes care of closing the file when it is no longer needed.

To use the `open` function, one needs to import the necessary modules such as `std::fs::File`, `std::io::prelude::*`, and `std::path::Path`. The `File::open` method is then called with the path as an argument. If the file is successfully opened, the function returns a `Result<File, io::Error>` object, otherwise, it panics with an error message.

Once the file is opened, its contents can be read using the `read_to_string` method. This method reads the contents of the file into a string and returns a `Result<usize, io::Error>`. If the reading operation is successful, the string will contain the file contents. Otherwise, it panics with an error message.

In the example provided, the contents of the `hello.txt` file are read and printed to the console. The `drop` trait is used to ensure that the file is closed when the `file` object goes out of scope.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.
