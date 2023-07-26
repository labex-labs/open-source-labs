# Matching Literals

As you saw in Chapter 6, you can match patterns against literals directly. The
following code gives some examples:

Filename: `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

This code prints `one` because the value in `x` is `1`. This syntax is useful
when you want your code to take an action if it gets a particular concrete
value.
