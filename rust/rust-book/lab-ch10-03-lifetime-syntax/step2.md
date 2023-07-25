# Preventing Dangling References with Lifetimes

The main aim of lifetimes is to prevent _dangling references_, which cause a
program to reference data other than the data it’s intended to reference.
Consider the program in Listing 10-16, which has an outer scope and an inner
scope.

```rust
fn main() {
  1 let r;

    {
      2 let x = 5;
      3 r = &x;
  4 }

  5 println!("r: {r}");
}
```

Listing 10-16: An attempt to use a reference whose value has gone out of scope

> Note: The examples in Listing 10-16, 10-17, and 10-23 declare variables
> without giving them an initial value, so the variable name exists in the outer
> scope. At first glance, this might appear to be in conflict with Rust’s having
> no null values. However, if we try to use a variable before giving it a value,
> we’ll get a compile-time error, which shows that Rust indeed does not allow
> null values.

The outer scope declares a variable named `r` with no initial value [1], and
the inner scope declares a variable named `x` with the initial value of `5`
[2]. Inside the inner scope, we attempt to set the value of `r` as a reference
to `x` [3]. Then the inner scope ends [4], and we attempt to print the value in
`r` [5]. This code won’t compile because the value that `r` is referring to has
gone out of scope before we try to use it. Here is the error message:

```bash
error[E0597]: `x` does not live long enough
 --> src/main.rs:6:13
  |
6 |         r = &x;
  |             ^^ borrowed value does not live long enough
7 |     }
  |     - `x` dropped here while still borrowed
8 |
9 |     println!("r: {r}");
  |                   - borrow later used here
```

The error message says that the variable `x` “does not live long enough.” The
reason is that `x` will be out of scope when the inner scope ends on line 7.
But `r` is still valid for the outer scope; because its scope is larger, we say
that it “lives longer.” If Rust allowed this code to work, `r` would be
referencing memory that was deallocated when `x` went out of scope, and
anything we tried to do with `r` wouldn’t work correctly. So how does Rust
determine that this code is invalid? It uses a borrow checker.
