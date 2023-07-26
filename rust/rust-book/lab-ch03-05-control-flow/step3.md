# Handling Multiple Conditions with else if

You can use multiple conditions by combining `if` and `else` in an `else if`
expression. For example:

Filename: `src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

This program has four possible paths it can take. After running it, you should
see the following output:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

When this program executes, it checks each `if` expression in turn and executes
the first body for which the condition evaluates to `true`. Note that even
though 6 is divisible by 2, we don’t see the output `number is divisible by 2`,
nor do we see the `number is not divisible by 4, 3, or 2` text from the `else`
block. That’s because Rust only executes the block for the first `true`
condition, and once it finds one, it doesn’t even check the rest.

Using too many `else if` expressions can clutter your code, so if you have more
than one, you might want to refactor your code. Chapter 6 describes a powerful
Rust branching construct called `match` for these cases.
