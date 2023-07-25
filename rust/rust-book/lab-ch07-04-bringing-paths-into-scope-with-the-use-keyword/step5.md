# Using External Packages

In Chapter 2, we programmed a guessing game project that used an external
package called `rand` to get random numbers. To use `rand` in our project, we
added this line to `Cargo.toml`:

Filename: `Cargo.toml`

```tomltoml
rand = "0.8.5"
```

Adding `rand` as a dependency in `Cargo.toml` tells Cargo to download the
`rand` package and any dependencies from *https://crates.io*, and make `rand`
available to our project.

Then, to bring `rand` definitions into the scope of our package, we added a
`use` line starting with the name of the crate, `rand`, and listed the items we
wanted to bring into scope. Recall that in “Generating a Random Number” on page
XX, we brought the `Rng` trait into scope and called the `rand::thread_rng`
function:

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Members of the Rust community have made many packages available at
*https://crates.io*, and pulling any of them into your package involves these
same steps: listing them in your package’s `Cargo.toml` file and using `use` to
bring items from their crates into scope.

Note that the standard `std` library is also a crate that’s external to our
package. Because the standard library is shipped with the Rust language, we
don’t need to change `Cargo.toml` to include `std`. But we do need to refer to
it with `use` to bring items from there into our package’s scope. For example,
with `HashMap` we would use this line:

```rust
use std::collections::HashMap;
```

This is an absolute path starting with `std`, the name of the standard library
crate.
