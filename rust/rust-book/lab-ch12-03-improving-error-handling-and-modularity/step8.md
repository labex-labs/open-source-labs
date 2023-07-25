# Returning a Result Instead of Calling panic!

We can instead return a `Result` value that will contain a `Config` instance in
the successful case and will describe the problem in the error case. We’re also
going to change the function name from `new` to `build` because many
programmers expect `new` functions to never fail. When `Config::build` is
communicating to `main`, we can use the `Result` type to signal there was a
problem. Then we can change `main` to convert an `Err` variant into a more
practical error for our users without the surrounding text about `thread
'main'` and `RUST_BACKTRACE` that a call to `panic!` causes.

Listing 12-9 shows the changes we need to make to the return value of the
function we’re now calling `Config::build` and the body of the function needed
to return a `Result`. Note that this won’t compile until we update `main` as
well, which we’ll do in the next listing.

Filename: `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

Listing 12-9: Returning a `Result` from `Config::build`

Our `build` function returns a `Result` with a `Config` instance in the success
case and an `&'static str` in the error case. Our error values will always be
string literals that have the `'static` lifetime.

We’ve made two changes in the body of the function: instead of calling `panic!`
when the user doesn’t pass enough arguments, we now return an `Err` value, and
we’ve wrapped the `Config` return value in an `Ok`. These changes make the
function conform to its new type signature.

Returning an `Err` value from `Config::build` allows the `main` function to
handle the `Result` value returned from the `build` function and exit the
process more cleanly in the error case.

#
