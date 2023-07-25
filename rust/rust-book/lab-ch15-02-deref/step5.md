# Implementing the Deref Trait

As discussed in “Implementing a Trait on a Type” on page XX, to implement a
trait we need to provide implementations for the trait’s required methods. The
`Deref` trait, provided by the standard library, requires us to implement one
method named `deref` that borrows `self` and returns a reference to the inner
data. Listing 15-10 contains an implementation of `Deref` to add to the
definition of ` MyBox``<T> `.

Filename: `src/main.rs`

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
  1 type Target = T;

    fn deref(&self) -> &Self::Target {
      2 &self.0
    }
}
```

Listing 15-10: Implementing `Deref` on `MyBox<T>`

The `type Target = T;` syntax [1] defines an associated type for the `Deref`
trait to use. Associated types are a slightly different way of declaring a
generic parameter, but you don’t need to worry about them for now; we’ll cover
them in more detail in Chapter 19.

We fill in the body of the `deref` method with `&self.0` so `deref` returns a
reference to the value we want to access with the `*` operator [2]; recall from
“Using Tuple Structs Without Named Fields to Create Different Types” on page XX
that `.0` accesses the first value in a tuple struct. The `main` function in
Listing 15-9 that calls `*` on the `MyBox<T>` value now compiles, and the
assertions pass!

Without the `Deref` trait, the compiler can only dereference `&` references.
The `deref` method gives the compiler the ability to take a value of any type
that implements `Deref` and call the `deref` method to get a `&` reference that
it knows how to dereference.

When we entered `*y` in Listing 15-9, behind the scenes Rust actually ran this
code:

```rust
*(y.deref())
```

Rust substitutes the `*` operator with a call to the `deref` method and then a
plain dereference so we don’t have to think about whether or not we need to
call the `deref` method. This Rust feature lets us write code that functions
identically whether we have a regular reference or a type that implements
`Deref`.

The reason the `deref` method returns a reference to a value, and that the
plain dereference outside the parentheses in `*(y.deref())` is still necessary,
has to do with the ownership system. If the `deref` method returned the value
directly instead of a reference to the value, the value would be moved out of
`self`. We don’t want to take ownership of the inner value inside `MyBox<T>` in
this case or in most cases where we use the dereference operator.

Note that the `*` operator is replaced with a call to the `deref` method and
then a call to the `*` operator just once, each time we use a `*` in our code.
Because the substitution of the `*` operator does not recurse infinitely, we
end up with data of type `i32`, which matches the `5` in `assert_eq!` in
Listing 15-9.
