# The match Control Flow Construct

Rust has an extremely powerful control flow construct called `match` that
allows you to compare a value against a series of patterns and then execute
code based on which pattern matches. Patterns can be made up of literal values,
variable names, wildcards, and many other things; Chapter 18 covers all the
different kinds of patterns and what they do. The power of `match` comes from
the expressiveness of the patterns and the fact that the compiler confirms that
all possible cases are handled.

Think of a `match` expression as being like a coin-sorting machine: coins slide
down a track with variously sized holes along it, and each coin falls through
the first hole it encounters that it fits into. In the same way, values go
through each pattern in a `match`, and at the first pattern the value “fits,”
the value falls into the associated code block to be used during execution.

Speaking of coins, let’s use them as an example using `match`! We can write a
function that takes an unknown US coin and, in a similar way as the counting
machine, determines which coin it is and returns its value in cents, as shown
in Listing 6-3.

```rust
1 enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
  2 match coin {
      3 Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

Listing 6-3: An enum and a `match` expression that has the variants of the enum
as its patterns

Let’s break down the `match` in the `value_in_cents` function. First we list
the `match` keyword followed by an expression, which in this case is the value
`coin` [2]. This seems very similar to an expression used with `if`, but
there’s a big difference: with `if`, the expression needs to return a Boolean
value, but here it can return any type. The type of `coin` in this example is
the `Coin` enum that we defined at [1].

Next are the `match` arms. An arm has two parts: a pattern and some code. The
first arm here has a pattern that is the value `Coin::Penny` and then the `=>`
operator that separates the pattern and the code to run [3]. The code in this
case is just the value `1`. Each arm is separated from the next with a comma.

When the `match` expression executes, it compares the resultant value against
the pattern of each arm, in order. If a pattern matches the value, the code
associated with that pattern is executed. If that pattern doesn’t match the
value, execution continues to the next arm, much as in a coin-sorting machine.
We can have as many arms as we need: in Listing 6-3, our `match` has four arms.

The code associated with each arm is an expression, and the resultant value of
the expression in the matching arm is the value that gets returned for the
entire `match` expression.

We don’t typically use curly brackets if the match arm code is short, as it is
in Listing 6-3 where each arm just returns a value. If you want to run multiple
lines of code in a match arm, you must use curly brackets, and the comma
following the arm is then optional. For example, the following code prints
“Lucky penny!” every time the method is called with a `Coin::Penny`, but still
returns the last value of the block, `1`:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
