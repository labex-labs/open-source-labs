# Matching Ranges of Values with ..=

The `..=` syntax allows us to match to an inclusive range of values. In the
following code, when a pattern matches any of the values within the given
range, that arm will execute:

Filename: `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    _ => println!("something else"),
}
```

If `x` is `1`, `2`, `3`, `4`, or `5`, the first arm will match. This syntax is
more convenient for multiple match values than using the `|` operator to
express the same idea; if we were to use `|`, we would have to specify `1 | 2 |
3 | 4 | 5`. Specifying a range is much shorter, especially if we want to match,
say, any number between 1 and 1,000!

The compiler checks that the range isn’t empty at compile time, and because the
only types for which Rust can tell if a range is empty or not are `char` and
numeric values, ranges are only allowed with numeric or `char` values.

Here is an example using ranges of `char` values:

Filename: `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("early ASCII letter"),
    'k'..='z' => println!("late ASCII letter"),
    _ => println!("something else"),
}
```

Rust can tell that `'c'` is within the first pattern’s range and prints `early
ASCII letter`.
