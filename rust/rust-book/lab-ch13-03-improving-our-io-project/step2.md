# Removing a clone Using an Iterator

In Listing 12-6, we added code that took a slice of `String` values and created
an instance of the `Config` struct by indexing into the slice and cloning the
values, allowing the `Config` struct to own those values. In Listing 13-17,
we’ve reproduced the implementation of the `Config::build` function as it was
in Listing 12-23.

Filename: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 13-17: Reproduction of the `Config::build` function from Listing 12-23

At the time, we said not to worry about the inefficient `clone` calls because
we would remove them in the future. Well, that time is now!

We needed `clone` here because we have a slice with `String` elements in the
parameter `args`, but the `build` function doesn’t own `args`. To return
ownership of a `Config` instance, we had to clone the values from the `query`
and `filename` fields of `Config` so the `Config` instance can own its values.

With our new knowledge about iterators, we can change the `build` function to
take ownership of an iterator as its argument instead of borrowing a slice.
We’ll use the iterator functionality instead of the code that checks the length
of the slice and indexes into specific locations. This will clarify what the
`Config::build` function is doing because the iterator will access the values.

Once `Config::build` takes ownership of the iterator and stops using indexing
operations that borrow, we can move the `String` values from the iterator into
`Config` rather than calling `clone` and making a new allocation.

#
