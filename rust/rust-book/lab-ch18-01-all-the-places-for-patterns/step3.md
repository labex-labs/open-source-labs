# Conditional if let Expressions

In Chapter 6, we discussed how to use `if let` expressions mainly as a shorter
way to write the equivalent of a `match` that only matches one case.
Optionally, `if let` can have a corresponding `else` containing code to run if
the pattern in the `if let` doesn’t match.

Listing 18-1 shows that it’s also possible to mix and match `if let`, `else
if`, and `else if let` expressions. Doing so gives us more flexibility than a
`match` expression in which we can express only one value to compare with the
patterns. Also, Rust doesn’t require that the conditions in a series of `if
let`, `else if`, and `else if let` arms relate to each other.

The code in Listing 18-1 determines what color to make your background based on
a series of checks for several conditions. For this example, we’ve created
variables with hardcoded values that a real program might receive from user
input.

Filename: `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listing 18-1: Mixing `if let`, `else if`, `else if let`, and `else`

If the user specifies a favorite color [1], that color is used as the
background [2]. If no favorite color is specified and today is Tuesday [3], the
background color is green [4]. Otherwise, if the user specifies their age as a
string and we can parse it as a number successfully [5], the color is either
purple [7] or orange [8] depending on the value of the number [6]. If none of
these conditions apply [9], the background color is blue [10].

This conditional structure lets us support complex requirements. With the
hardcoded values we have here, this example will print `Using purple as the
background color`.

You can see that `if let` can also introduce shadowed variables in the same way
that `match` arms can: the line `if let Ok(age) = age` [5] introduces a new
shadowed `age` variable that contains the value inside the `Ok` variant. This
means we need to place the `if age > 30` condition [6] within that block: we
can’t combine these two conditions into `if let Ok(age) = age && age > 30`. The
shadowed `age` we want to compare to 30 isn’t valid until the new scope starts
with the curly bracket.

The downside of using `if let` expressions is that the compiler doesn’t check
for exhaustiveness, whereas with `match` expressions it does. If we omitted the
last `else` block [9] and therefore missed handling some cases, the compiler
would not alert us to the possible logic bug.
