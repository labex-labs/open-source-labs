# How Deref Coercion Interacts with Mutability

Similar to how you use the `Deref` trait to override the `*` operator on
immutable references, you can use the `DerefMut` trait to override the `*`
operator on mutable references.

Rust does deref coercion when it finds types and trait implementations in three
cases:

- From `&T` to `&U` when `T: Deref<Target=U>`
- From `&mut T` to `&mut U` when `T: DerefMut<Target=U>`
- From `&mut T` to `&U` when `T: Deref<Target=U>`

The first two cases are the same except that the second implements mutability.
The first case states that if you have a `&T`, and `T` implements `Deref` to
some type `U`, you can get a `&U` transparently. The second case states that
the same deref coercion happens for mutable references.

The third case is trickier: Rust will also coerce a mutable reference to an
immutable one. But the reverse is _not_ possible: immutable references will
never coerce to mutable references. Because of the borrowing rules, if you have
a mutable reference, that mutable reference must be the only reference to that
data (otherwise, the program wouldn’t compile). Converting one mutable
reference to one immutable reference will never break the borrowing rules.
Converting an immutable reference to a mutable reference would require that the
initial immutable reference is the only immutable reference to that data, but
the borrowing rules don’t guarantee that. Therefore, Rust can’t make the
assumption that converting an immutable reference to a mutable reference is
possible.
