# Propagating Errors

When a function’s implementation calls something that might fail, instead of
handling the error within the function itself you can return the error to the
calling code so that it can decide what to do. This is known as _propagating_
the error and gives more control to the calling code, where there might be more
information or logic that dictates how the error should be handled than what
you have available in the context of your code.

For example, Listing 9-6 shows a function that reads a username from a file. If
the file doesn’t exist or can’t be read, this function will return those errors
to the code that called the function.

Filename: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

Listing 9-6: A function that returns errors to the calling code using `match`

This function can be written in a much shorter way, but we’re going to start by
doing a lot of it manually in order to explore error handling; at the end,
we’ll show the shorter way. Let’s look at the return type of the function
first: `Result<String, io::Error>` [1]. This means the function is returning a
value of the type `Result<T, E>`, where the generic parameter `T` has been
filled in with the concrete type `String` and the generic type `E` has been
filled in with the concrete type `io::Error`.

If this function succeeds without any problems, the code that calls this
function will receive an `Ok` value that holds a `String`—the `username` that
this function read from the file [8]. If this function encounters any problems,
the calling code will receive an `Err` value that holds an instance of
`io::Error` that contains more information about what the problems were. We
chose `io::Error` as the return type of this function because that happens to
be the type of the error value returned from both of the operations we’re
calling in this function’s body that might fail: the `File::open` function [2]
and the `read_to_string` method [7].

The body of the function starts by calling the `File::open` function [2]. Then
we handle the `Result` value with a `match` similar to the `match` in Listing
9-4. If `File::open` succeeds, the file handle in the pattern variable `file`
[4] becomes the value in the mutable variable `username_file` [3] and the
function continues. In the `Err` case, instead of calling `panic!`, we use the
`return` keyword to return early out of the function entirely and pass the
error value from `File::open`, now in the pattern variable `e`, back to the
calling code as this function’s error value [5].

So, if we have a file handle in `username_file`, the function then creates a
new `String` in variable `username` [6] and calls the `read_to_string` method
on the file handle in `username_file` to read the contents of the file into
`username` [7]. The `read_to_string` method also returns a `Result` because it
might fail, even though `File::open` succeeded. So we need another `match` to
handle that `Result`: if `read_to_string` succeeds, then our function has
succeeded, and we return the username from the file that’s now in `username`
wrapped in an `Ok`. If `read_to_string` fails, we return the error value in the
same way that we returned the error value in the `match` that handled the
return value of `File::open`. However, we don’t need to explicitly say
`return`, because this is the last expression in the function [9].

The code that calls this code will then handle getting either an `Ok` value
that contains a username or an `Err` value that contains an `io::Error`. It’s
up to the calling code to decide what to do with those values. If the calling
code gets an `Err` value, it could call `panic!` and crash the program, use a
default username, or look up the username from somewhere other than a file, for
example. We don’t have enough information on what the calling code is actually
trying to do, so we propagate all the success or error information upward for
it to handle appropriately.

This pattern of propagating errors is so common in Rust that Rust provides the
question mark operator `?` to make this easier.

#
