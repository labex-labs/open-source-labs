# Multiple Patterns

In `match` expressions, you can match multiple patterns using the `|` syntax,
which is the pattern _or_ operator. For example, in the following code we match
the value of `x` against the match arms, the first of which has an _or_ option,
meaning if the value of `x` matches either of the values in that arm, that
arm’s code will run:

Filename: `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

This code prints `one or two`.
