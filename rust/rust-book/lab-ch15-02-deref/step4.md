# Defining Our Own Smart Pointer

Let’s build a smart pointer similar to the `Box<T>` type provided by the
standard library to experience how smart pointers behave differently from
references by default. Then we’ll look at how to add the ability to use the
dereference operator.

The `Box<T>` type is ultimately defined as a tuple struct with one element, so
Listing 15-8 defines a `MyBox<T>` type in the same way. We’ll also define a
`new` function to match the `new` function defined on `Box<T>`.

Filename: `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Listing 15-8: Defining a `MyBox<T>` type

We define a struct named `MyBox` and declare a generic parameter `T` [1]
because we want our type to hold values of any type. The `MyBox` type is a
tuple struct with one element of type `T`. The `MyBox::new` function takes one
parameter of type `T` [2] and returns a `MyBox` instance that holds the value
passed in [3].

Let’s try adding the `main` function in Listing 15-7 to Listing 15-8 and
changing it to use the `MyBox<T>` type we’ve defined instead of `Box<T>`. The
code in Listing 15-9 won’t compile because Rust doesn’t know how to dereference
`MyBox`.

Filename: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Listing 15-9: Attempting to use `MyBox<T>` in the same way we used references
and `Box<T>`

Here’s the resultant compilation error:

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

Our `MyBox<T>` type can’t be dereferenced because we haven’t implemented that
ability on our type. To enable dereferencing with the `*` operator, we
implement the `Deref` trait.
