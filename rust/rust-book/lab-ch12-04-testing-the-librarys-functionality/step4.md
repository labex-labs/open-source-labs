# Iterating Through Lines with the lines Method

Rust has a helpful method to handle line-by-line iteration of strings,
conveniently named `lines`, that works as shown in Listing 12-17. Note that
this won’t compile yet.

Filename: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // do something with line
    }
}
```

Listing 12-17: Iterating through each line in `contents`

The `lines` method returns an iterator. We’ll talk about iterators in depth in
Chapter 13, but recall that you saw this way of using an iterator in Listing
3-5, where we used a `for` loop with an iterator to run some code on each item
in a collection.
