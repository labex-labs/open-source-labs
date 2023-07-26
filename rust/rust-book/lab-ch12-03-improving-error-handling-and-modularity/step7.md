# Improving the Error Message

In Listing 12-8, we add a check in the `new` function that will verify that the
slice is long enough before accessing index 1 and index 2. If the slice isn’t
long enough, the program panics and displays a better error message.

Filename: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

Listing 12-8: Adding a check for the number of arguments

This code is similar to the `Guess::new` function we wrote in Listing 9-13,
where we called `panic!` when the `value` argument was out of the range of
valid values. Instead of checking for a range of values here, we’re checking
that the length of `args` is at least `3` and the rest of the function can
operate under the assumption that this condition has been met. If `args` has
fewer than three items, this condition will be `true`, and we call the `panic!`
macro to end the program immediately.

With these extra few lines of code in `new`, let’s run the program without any
arguments again to see what the error looks like now:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

This output is better: we now have a reasonable error message. However, we also
have extraneous information we don’t want to give to our users. Perhaps the
technique we used in Listing 9-13 isn’t the best one to use here: a call to
`panic!` is more appropriate for a programming problem than a usage problem, as
discussed in Chapter 9. Instead, we’ll use the other technique you learned
about in Chapter 9—returning a `Result` that indicates either success or an
error.
