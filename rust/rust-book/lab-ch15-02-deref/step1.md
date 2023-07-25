# Treating Smart Pointers Like Regular References with Deref

Implementing the `Deref` trait allows you to customize the behavior of the
_dereference operator_ `*` (not to be confused with the multiplication or glob
operator). By implementing `Deref` in such a way that a smart pointer can be
treated like a regular reference, you can write code that operates on
references and use that code with smart pointers too.

Let’s first look at how the dereference operator works with regular references.
Then we’ll try to define a custom type that behaves like `Box<T>`, and see why
the dereference operator doesn’t work like a reference on our newly defined
type. We’ll explore how implementing the `Deref` trait makes it possible for
smart pointers to work in ways similar to references. Then we’ll look at Rust’s
_deref coercion_ feature and how it lets us work with either references or
smart pointers.

> Note: There’s one big difference between the `MyBox<T>` type we’re about to
> build and the real `Box<T>`: our version will not store its data on the heap.
> We are focusing this example on `Deref`, so where the data is actually stored
> is less important than the pointer-like behavior.
