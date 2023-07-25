# for Loops

In a `for` loop, the value that directly follows the keyword `for` is a
pattern. For example, in `for x in y`, the `x` is the pattern. Listing 18-3
demonstrates how to use a pattern in a `for` loop to _destructure_, or break
apart, a tuple as part of the `for` loop.

Filename: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listing 18-3: Using a pattern in a `for` loop to destructure a tuple

The code in Listing 18-3 will print the following:

```
a is at index 0
b is at index 1
c is at index 2
```

We adapt an iterator using the `enumerate` method so it produces a value and
the index for that value, placed into a tuple. The first value produced is the
tuple `(0, 'a')`. When this value is matched to the pattern `(index, value)`,
`index` will be `0` and `value` will be `'a'`, printing the first line of the
output.
