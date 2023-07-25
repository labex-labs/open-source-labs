# Trait Bound Syntax

The `impl Trait` syntax works for straightforward cases but is actually syntax
sugar for a longer form known as a _trait bound_; it looks like this:

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

This longer form is equivalent to the example in the previous section but is
more verbose. We place trait bounds with the declaration of the generic type
parameter after a colon and inside angle brackets.

The `impl Trait` syntax is convenient and makes for more concise code in simple
cases, while the fuller trait bound syntax can express more complexity in other
cases. For example, we can have two parameters that implement `Summary`. Doing
so with the `impl Trait` syntax looks like this:

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

Using `impl Trait` is appropriate if we want this function to allow `item1` and
`item2` to have different types (as long as both types implement `Summary`). If
we want to force both parameters to have the same type, however, we must use a
trait bound, like this:

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

The generic type `T` specified as the type of the `item1` and `item2`
parameters constrains the function such that the concrete type of the value
passed as an argument for `item1` and `item2` must be the same.

#
