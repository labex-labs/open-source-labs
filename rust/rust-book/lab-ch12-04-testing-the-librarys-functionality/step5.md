# Searching Each Line for the Query

Next, we’ll check whether the current line contains our query string.
Fortunately, strings have a helpful method named `contains` that does this for
us! Add a call to the `contains` method in the `search` function, as shown in
Listing 12-18. Note that this still won’t compile yet.

Filename: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // do something with line
        }
    }
}
```

Listing 12-18: Adding functionality to see whether the line contains the string
in `query`

At the moment, we’re building up functionality. To get the code to compile, we
need to return a value from the body as we indicated we would in the function
signature.

#
