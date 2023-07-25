# while let Conditional Loops

Similar in construction to `if let`, the `while let` conditional loop allows a
`while` loop to run for as long as a pattern continues to match. In Listing
18-2, we code a `while let` loop that uses a vector as a stack and prints the
values in the vector in the opposite order in which they were pushed.

Filename: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listing 18-2: Using a `while let` loop to print values for as long as
`stack.pop()` returns `Some`

This example prints `3`, `2`, and then `1`. The `pop` method takes the last
element out of the vector and returns `Some(value)`. If the vector is empty,
`pop` returns `None`. The `while` loop continues running the code in its block
as long as `pop` returns `Some`. When `pop` returns `None`, the loop stops. We
can use `while let` to pop every element off our stack.
