# Destructuring Enums

We’ve destructured enums in this book (for example, Listing 6-5), but we
haven’t yet explicitly discussed that the pattern to destructure an enum
corresponds to the way the data stored within the enum is defined. As an
example, in Listing 18-15 we use the `Message` enum from Listing 6-2 and write
a `match` with patterns that will destructure each inner value.

Filename: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

Listing 18-15: Destructuring enum variants that hold different kinds of values

This code will print `Change color to red 0, green 160, and blue 255`. Try
changing the value of `msg` [1] to see the code from the other arms run.

For enum variants without any data, like `Message::Quit` [2], we can’t
destructure the value any further. We can only match on the literal
`Message::Quit` value, and no variables are in that pattern.

For struct-like enum variants, such as `Message::Move` [3], we can use a
pattern similar to the pattern we specify to match structs. After the variant
name, we place curly brackets and then list the fields with variables so we
break apart the pieces to use in the code for this arm. Here we use the
shorthand form as we did in Listing 18-13.

For tuple-like enum variants, like `Message::Write` that holds a tuple with one
element [4] and `Message::ChangeColor` that holds a tuple with three elements
[5], the pattern is similar to the pattern we specify to match tuples. The
number of variables in the pattern must match the number of elements in the
variant we’re matching.
