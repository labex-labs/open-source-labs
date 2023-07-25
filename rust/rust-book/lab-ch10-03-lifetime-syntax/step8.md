# Lifetime Annotations in Struct Definitions

So far, the structs we’ve defined all hold owned types. We can define structs
to hold references, but in that case we would need to add a lifetime annotation
on every reference in the struct’s definition. Listing 10-24 has a struct named
`ImportantExcerpt` that holds a string slice.

Filename: `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
        .split('.')
        .next()
        .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Listing 10-24: A struct that holds a reference, requiring a lifetime annotation

This struct has the single field `part` that holds a string slice, which is a
reference [2]. As with generic data types, we declare the name of the generic
lifetime parameter inside angle brackets after the name of the struct so we can
use the lifetime parameter in the body of the struct definition [1]. This
annotation means an instance of `ImportantExcerpt` can’t outlive the reference
it holds in its `part` field.

The `main` function here creates an instance of the `ImportantExcerpt` struct
[5] that holds a reference to the first sentence of the `String` [4] owned by
the variable `novel` [3]. The data in `novel` exists before the
`ImportantExcerpt` instance is created. In addition, `novel` doesn’t go out of
scope until after the `ImportantExcerpt` goes out of scope, so the reference in
the `ImportantExcerpt` instance is valid.
