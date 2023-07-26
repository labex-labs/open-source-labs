# RefCell<T> and the Interior Mutability Pattern

_Interior mutability_ is a design pattern in Rust that allows you to mutate
data even when there are immutable references to that data; normally, this
action is disallowed by the borrowing rules. To mutate data, the pattern uses
`unsafe` code inside a data structure to bend Rust’s usual rules that govern
mutation and borrowing. Unsafe code indicates to the compiler that we’re
checking the rules manually instead of relying on the compiler to check them
for us; we will discuss unsafe code more in Chapter 19.

We can use types that use the interior mutability pattern only when we can
ensure that the borrowing rules will be followed at runtime, even though the
compiler can’t guarantee that. The `unsafe` code involved is then wrapped in a
safe API, and the outer type is still immutable.

Let’s explore this concept by looking at the `RefCell<T>` type that follows the
interior mutability pattern.
