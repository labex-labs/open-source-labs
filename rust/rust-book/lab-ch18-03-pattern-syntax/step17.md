# @ Bindings

The _at_ operator `@` lets us create a variable that holds a value at the same
time we’re testing that value for a pattern match. In Listing 18-29, we want to
test that a `Message::Hello` `id` field is within the range `3..=7`. We also
want to bind the value to the variable `id_variable` so we can use it in the
code associated with the arm. We could name this variable `id`, the same as the
field, but for this example we’ll use a different name.

Filename: `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Found an id in range: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Found an id in another range")
    }
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

Listing 18-29: Using `@` to bind to a value in a pattern while also testing it

This example will print `Found an id in range: 5`. By specifying `id_variable
@` before the range `3..=7`, we’re capturing whatever value matched the range
while also testing that the value matched the range pattern.

In the second arm, where we only have a range specified in the pattern, the
code associated with the arm doesn’t have a variable that contains the actual
value of the `id` field. The `id` field’s value could have been 10, 11, or 12,
but the code that goes with that pattern doesn’t know which it is. The pattern
code isn’t able to use the value from the `id` field because we haven’t saved
the `id` value in a variable.

In the last arm, where we’ve specified a variable without a range, we do have
the value available to use in the arm’s code in a variable named `id`. The
reason is that we’ve used the struct field shorthand syntax. But we haven’t
applied any test to the value in the `id` field in this arm, as we did with the
first two arms: any value would match this pattern.

Using `@` lets us test a value and save it in a variable within one pattern.
