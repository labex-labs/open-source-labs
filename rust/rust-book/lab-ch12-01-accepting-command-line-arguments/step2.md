# Reading the Argument Values

To enable `minigrep` to read the values of command line arguments we pass to
it, we’ll need the `std::env::args` function provided in Rust’s standard
library. This function returns an iterator of the command line arguments passed
to `minigrep`. We’ll cover iterators fully in Chapter 13. For now, you only
need to know two details about iterators: iterators produce a series of values,
and we can call the `collect` method on an iterator to turn it into a
collection, such as a vector, that contains all the elements the iterator
produces.

The code in Listing 12-1 allows your `minigrep` program to read any command
line arguments passed to it, and then collect the values into a vector.

Filename: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

Listing 12-1: Collecting the command line arguments into a vector and printing
them

First we bring the `std::env` module into scope with a `use` statement so we
can use its `args` function. Notice that the `std::env::args` function is
nested in two levels of modules. As we discussed in Chapter 7, in cases where
the desired function is nested in more than one module, we’ve chosen to bring
the parent module into scope rather than the function. By doing so, we can
easily use other functions from `std::env`. It’s also less ambiguous than
adding `use std::env::args` and then calling the function with just `args`,
because `args` might easily be mistaken for a function that’s defined in the
current module.

> **The args Function and Invalid Unicode**
>
> Note that `std::env::args` will panic if any argument contains invalid
> Unicode. If your program needs to accept arguments containing invalid Unicode,
> use `std::env::args_os` instead. That function returns an iterator that
> produces `OsString` values instead of `String` values. We’ve chosen to use
> `std::env::args` here for simplicity because `OsString` values differ per
> platform and are more complex to work with than `String` values.

On the first line of `main`, we call `env::args`, and we immediately use
`collect` to turn the iterator into a vector containing all the values produced
by the iterator. We can use the `collect` function to create many kinds of
collections, so we explicitly annotate the type of `args` to specify that we
want a vector of strings. Although you very rarely need to annotate types in
Rust, `collect` is one function you do often need to annotate because Rust
isn’t able to infer the kind of collection you want.

Finally, we print the vector using the debug macro. Let’s try running the code
first with no arguments and then with two arguments:

```bash
$ cargo run
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
]
$ cargo run -- needle haystack
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
"needle",
"haystack",
]
```

Notice that the first value in the vector is `"target/debug/minigrep"`, which
is the name of our binary. This matches the behavior of the arguments list in
C, letting programs use the name by which they were invoked in their execution.
It’s often convenient to have access to the program name in case you want to
print it in messages or change the behavior of the program based on what
command line alias was used to invoke the program. But for the purposes of this
chapter, we’ll ignore it and save only the two arguments we need.
