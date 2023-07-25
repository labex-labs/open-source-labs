# Destructuring Structs and Tuples

We can mix, match, and nest destructuring patterns in even more complex ways.
The following example shows a complicated destructure where we nest structs and
tuples inside a tuple and destructure all the primitive values out:

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

This code lets us break complex types into their component parts so we can use
the values we’re interested in separately.

Destructuring with patterns is a convenient way to use pieces of values, such
as the value from each field in a struct, separately from each other.
