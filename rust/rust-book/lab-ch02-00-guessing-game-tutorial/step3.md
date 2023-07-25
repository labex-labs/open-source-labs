# Processing a Guess

The first part of the guessing game program will ask for user input, process
that input, and check that the input is in the expected form. To start, we’ll
allow the player to input a guess. Enter the code in Listing 2-1 into
`src/main.rs`.

Filename: `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listing 2-1: Code that gets a guess from the user and prints it

This code contains a lot of information, so let’s go over it line by line. To
obtain user input and then print the result as output, we need to bring the
`io` input/output library into scope. The `io` library comes from the standard
library, known as `std`:

```rust
use std::io;
```

By default, Rust has a set of items defined in the standard library that it
brings into the scope of every program. This set is called the _prelude_, and
you can see everything in it at
*https://doc.rust-lang.org/std/prelude/index.html*.

If a type you want to use isn’t in the prelude, you have to bring that type
into scope explicitly with a `use` statement. Using the `std::io` library
provides you with a number of useful features, including the ability to accept
user input.

As you saw in Chapter 1, the `main` function is the entry point into the
program:

```rust
fn main() {
```

The `fn` syntax declares a new function; the parentheses, `()`, indicate there
are no parameters; and the curly bracket, `{`, starts the body of the function.

As you also learned in Chapter 1, `println!` is a macro that prints a string to
the screen:

```
println!("Guess the number!");

println!("Please input your guess.");
```

This code is printing a prompt stating what the game is and requesting input
from the user.
