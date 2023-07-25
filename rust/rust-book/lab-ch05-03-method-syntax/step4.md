# Associated Functions

All functions defined within an `impl` block are called _associated functions_
because they’re associated with the type named after the `impl`. We can define
associated functions that don’t have `self` as their first parameter (and thus
are not methods) because they don’t need an instance of the type to work with.
We’ve already used one function like this: the `String::from` function that’s
defined on the `String` type.

Associated functions that aren’t methods are often used for constructors that
will return a new instance of the struct. These are often called `new`, but
`new` isn’t a special name and isn’t built into the language. For example, we
could choose to provide an associated function named `square` that would have
one dimension parameter and use that as both width and height, thus making it
easier to create a square `Rectangle` rather than having to specify the same
value twice:

Filename: `src/main.rs`

```rust
impl Rectangle {
    fn square(size: u32) -> 1 Self  {
      2 Self  {
            width: size,
            height: size,
        }
    }
}
```

The `Self` keywords in the return type [1] and in the body of the function [2]
are aliases for the type that appears after the `impl` keyword, which in this
case is `Rectangle`.

To call this associated function, we use the `::` syntax with the struct name;
`let sq = Rectangle::square(3);` is an example. This function is namespaced by
the struct: the `::` syntax is used for both associated functions and
namespaces created by modules. We’ll discuss modules in Chapter 7.
