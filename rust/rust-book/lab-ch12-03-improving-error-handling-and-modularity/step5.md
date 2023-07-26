# Creating a Constructor for Config

So far, we’ve extracted the logic responsible for parsing the command line
arguments from `main` and placed it in the `parse_config` function. Doing so
helped us see that the `query` and `file_path` values were related, and that
relationship should be conveyed in our code. We then added a `Config` struct to
name the related purpose of `query` and `file_path` and to be able to return
the values’ names as struct field names from the `parse_config` function.

So now that the purpose of the `parse_config` function is to create a `Config`
instance, we can change `parse_config` from a plain function to a function
named `new` that is associated with the `Config` struct. Making this change
will make the code more idiomatic. We can create instances of types in the
standard library, such as `String`, by calling `String::new`. Similarly, by
changing `parse_config` into a `new` function associated with `Config`, we’ll
be able to create instances of `Config` by calling `Config::new`. Listing 12-7
shows the changes we need to make.

Filename: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Listing 12-7: Changing `parse_config` into `Config::new`

We’ve updated `main` where we were calling `parse_config` to instead call
`Config::new` [1]. We’ve changed the name of `parse_config` to `new` [3] and
moved it within an `impl` block [2], which associates the `new` function with
`Config`. Try compiling this code again to make sure it works.
