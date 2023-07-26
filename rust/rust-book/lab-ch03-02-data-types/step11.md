# Accessing Array Elements

An array is a single chunk of memory of a known, fixed size that can be
allocated on the stack. You can access elements of an array using indexing,
like this:

Filename: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

In this example, the variable named `first` will get the value `1` because that
is the value at index `[0]` in the array. The variable named `second` will get
the value `2` from index `[1]` in the array.
