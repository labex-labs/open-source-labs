# An Unused Variable by Starting Its Name with \_

If you create a variable but don’t use it anywhere, Rust will usually issue a
warning because an unused variable could be a bug. However, sometimes it’s
useful to be able to create a variable you won’t use yet, such as when you’re
prototyping or just starting a project. In this situation, you can tell Rust
not to warn you about the unused variable by starting the name of the variable
with an underscore. In Listing 18-20, we create two unused variables, but when
we compile this code, we should only get a warning about one of them.

Filename: `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Listing 18-20: Starting a variable name with an underscore to avoid getting
unused variable warnings

Here, we get a warning about not using the variable `y`, but we don’t get a
warning about not using `_x`.

Note that there is a subtle difference between using only `_` and using a name
that starts with an underscore. The syntax `_x` still binds the value to the
variable, whereas `_` doesn’t bind at all. To show a case where this
distinction matters, Listing 18-21 will provide us with an error.

Filename: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-21: An unused variable starting with an underscore still binds the
value, which might take ownership of the value.

We’ll receive an error because the `s` value will still be moved into `_s`,
which prevents us from using `s` again. However, using the underscore by itself
doesn’t ever bind to the value. Listing 18-22 will compile without any errors
because `s` doesn’t get moved into `_`.

Filename: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-22: Using an underscore does not bind the value.

This code works just fine because we never bind `s` to anything; it isn’t moved.
