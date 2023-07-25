# Returning Errors from the run Function

With the remaining program logic separated into the `run` function, we can
improve the error handling, as we did with `Config::build` in Listing 12-9.
Instead of allowing the program to panic by calling `expect`, the `run`
function will return a `Result<T, E>` when something goes wrong. This will let
us further consolidate the logic around handling errors into `main` in a
user-friendly way. Listing 12-12 shows the changes we need to make to the
signature and body of `run`.

Filename: `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3 ?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

Listing 12-12: Changing the `run` function to return `Result`

We’ve made three significant changes here. First, we changed the return type of
the `run` function to `Result<(), Box<dyn Error>>` [2]. This function
previously returned the unit type, `()`, and we keep that as the value returned
in the `Ok` case.

For the error type, we used the _trait object_ `Box<dyn Error>` (and we’ve
brought `std::error::Error` into scope with a `use` statement at the top [1]).
We’ll cover trait objects in Chapter 17. For now, just know that `Box<dyn
Error>` means the function will return a type that implements the `Error`
trait, but we don’t have to specify what particular type the return value will
be. This gives us flexibility to return error values that may be of different
types in different error cases. The `dyn` keyword is short for _dynamic_.

Second, we’ve removed the call to `expect` in favor of the `?` operator [3], as
we talked about in Chapter 9. Rather than `panic!` on an error, `?` will return
the error value from the current function for the caller to handle.

Third, the `run` function now returns an `Ok` value in the success case [4].
We’ve declared the `run` function’s success type as `()` in the signature,
which means we need to wrap the unit type value in the `Ok` value. This
`Ok(())` syntax might look a bit strange at first, but using `()` like this is
the idiomatic way to indicate that we’re calling `run` for its side effects
only; it doesn’t return a value we need.

When you run this code, it will compile but will display a warning:

```
warning: unused `Result` that must be used
  --> src/main.rs:19:5
   |
19 |     run(config);
   |     ^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be
handled
```

Rust tells us that our code ignored the `Result` value and the `Result` value
might indicate that an error occurred. But we’re not checking to see whether or
not there was an error, and the compiler reminds us that we probably meant to
have some error-handling code here! Let’s rectify that problem now.

#
