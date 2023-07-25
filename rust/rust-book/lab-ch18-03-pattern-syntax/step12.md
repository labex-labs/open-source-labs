# An Entire Value with \_

We’ve used the underscore as a wildcard pattern that will match any value but
not bind to the value. This is especially useful as the last arm in a `match`
expression, but we can also use it in any pattern, including function
parameters, as shown in Listing 18-17.

Filename: `src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("This code only uses the y parameter: {y}");
}

fn main() {
    foo(3, 4);
}
```

Listing 18-17: Using `_` in a function signature

This code will completely ignore the value `3` passed as the first argument,
and will print `This code only uses the y parameter: 4`.

In most cases when you no longer need a particular function parameter, you
would change the signature so it doesn’t include the unused parameter. Ignoring
a function parameter can be especially useful in cases when, for example,
you’re implementing a trait when you need a certain type signature but the
function body in your implementation doesn’t need one of the parameters. You
then avoid getting a compiler warning about unused function parameters, as you
would if you used a name instead.

#
