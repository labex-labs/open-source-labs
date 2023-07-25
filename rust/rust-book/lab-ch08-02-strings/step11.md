# Methods for Iterating Over Strings

The best way to operate on pieces of strings is to be explicit about whether
you want characters or bytes. For individual Unicode scalar values, use the
`chars` method. Calling `chars` on “Зд” separates out and returns two values of
type `char`, and you can iterate over the result to access each element:

```
for c in "Зд".chars() {
    println!("{c}");
}
```

This code will print the following:

```rust
З
д
```

Alternatively, the `bytes` method returns each raw byte, which might be
appropriate for your domain:

```
for b in "Зд".bytes() {
    println!("{b}");
}
```

This code will print the four bytes that make up this string:

```
208
151
208
180
```

But be sure to remember that valid Unicode scalar values may be made up of more
than one byte.

Getting grapheme clusters from strings, as with the Devanagari script, is
complex, so this functionality is not provided by the standard library. Crates
are available at *https://crates.io* if this is the functionality you need.
