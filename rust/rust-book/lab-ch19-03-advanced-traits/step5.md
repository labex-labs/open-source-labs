# Using Supertraits

Sometimes you might write a trait definition that depends on another trait: for
a type to implement the first trait, you want to require that type to also
implement the second trait. You would do this so that your trait definition can
make use of the associated items of the second trait. The trait your trait
definition is relying on is called a _supertrait_ of your trait.

For example, let’s say we want to make an `OutlinePrint` trait with an
`outline_print` method that will print a given value formatted so that it’s
framed in asterisks. That is, given a `Point` struct that implements the
standard library trait `Display` to result in `(x, y)`, when we call
`outline_print` on a `Point` instance that has `1` for `x` and `3` for `y`, it
should print the following:

```
**********
*        *
* (1, 3) *
*        *
**********
```

In the implementation of the `outline_print` method, we want to use the
`Display` trait’s functionality. Therefore, we need to specify that the
`OutlinePrint` trait will work only for types that also implement `Display` and
provide the functionality that `OutlinePrint` needs. We can do that in the
trait definition by specifying `OutlinePrint: Display`. This technique is
similar to adding a trait bound to the trait. Listing 19-22 shows an
implementation of the `OutlinePrint` trait.

Filename: `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Listing 19-22: Implementing the `OutlinePrint` trait that requires the
functionality from `Display`

Because we’ve specified that `OutlinePrint` requires the `Display` trait, we
can use the `to_string` function that is automatically implemented for any type
that implements `Display`. If we tried to use `to_string` without adding a
colon and specifying the `Display` trait after the trait name, we’d get an
error saying that no method named `to_string` was found for the type `&Self` in
the current scope.

Let’s see what happens when we try to implement `OutlinePrint` on a type that
doesn’t implement `Display`, such as the `Point` struct:

Filename: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

We get an error saying that `Display` is required but not implemented:

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

To fix this, we implement `Display` on `Point` and satisfy the constraint that
`OutlinePrint` requires, like so:

Filename: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Then, implementing the `OutlinePrint` trait on `Point` will compile
successfully, and we can call `outline_print` on a `Point` instance to display
it within an outline of asterisks.
