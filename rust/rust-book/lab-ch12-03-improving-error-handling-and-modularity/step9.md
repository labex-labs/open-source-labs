# Calling Config::build and Handling Errors

To handle the error case and print a user-friendly message, we need to update
`main` to handle the `Result` being returned by `Config::build`, as shown in
Listing 12-10. We’ll also take the responsibility of exiting the command line
tool with a nonzero error code away from `panic!` and instead implement it by
hand. A nonzero exit status is a convention to signal to the process that
called our program that the program exited with an error state.

Filename: `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

Listing 12-10: Exiting with an error code if building a `Config` fails

In this listing, we’ve used a method we haven’t covered in detail yet:
`unwrap_or_else`, which is defined on `Result<T, E>` by the standard library
[2]. Using `unwrap_or_else` allows us to define some custom, non-`panic!` error
handling. If the `Result` is an `Ok` value, this method’s behavior is similar
to `unwrap`: it returns the inner value that `Ok` is wrapping. However, if the
value is an `Err` value, this method calls the code in the _closure_, which is
an anonymous function we define and pass as an argument to `unwrap_or_else`
[3]. We’ll cover closures in more detail in Chapter 13. For now, you just need
to know that `unwrap_or_else` will pass the inner value of the `Err`, which in
this case is the static string `"not enough arguments"` that we added in
Listing 12-9, to our closure in the argument `err` that appears between the
vertical pipes [4]. The code in the closure can then use the `err` value when
it runs.

We’ve added a new `use` line to bring `process` from the standard library into
scope [1]. The code in the closure that will be run in the error case is only
two lines: we print the `err` value [5] and then call `process::exit` [6]. The
`process::exit` function will stop the program immediately and return the
number that was passed as the exit status code. This is similar to the
`panic!`-based handling we used in Listing 12-8, but we no longer get all the
extra output. Let’s try it:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

Great! This output is much friendlier for our users.
