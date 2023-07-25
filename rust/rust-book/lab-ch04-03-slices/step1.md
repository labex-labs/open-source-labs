# The Slice Type

_Slices_ let you reference a contiguous sequence of elements in a collection
rather than the whole collection. A slice is a kind of reference, so it does
not have ownership.

Here’s a small programming problem: write a function that takes a string of
words separated by spaces and returns the first word it finds in that string.
If the function doesn’t find a space in the string, the whole string must be
one word, so the entire string should be returned.

Let’s work through how we’d write the signature of this function without using
slices, to understand the problem that slices will solve:

```rust
fn first_word(s: &String) -> ?
```

The `first_word` function has a `&String` as a parameter. We don’t want
ownership, so this is fine. But what should we return? We don’t really have a
way to talk about _part_ of a string. However, we could return the index of the
end of the word, indicated by a space. Let’s try that, as shown in Listing 4-7.

Filename: `src/main.rs`

```rust
fn first_word(s: &String) -> usize {
  1 let bytes = s.as_bytes();

    for (2 i, &item) in 3 bytes.iter().enumerate() {
      4 if item == b' ' {
            return i;
        }
    }

  5 s.len()
}
```

Listing 4-7: The `first_word` function that returns a byte index value into the
`String` parameter

Because we need to go through the `String` element by element and check whether
a value is a space, we’ll convert our `String` to an array of bytes using the
`as_bytes` method [1].

Next, we create an iterator over the array of bytes using the `iter` method
[3]. We’ll discuss iterators in more detail in Chapter 13. For now, know that
`iter` is a method that returns each element in a collection and that
`enumerate` wraps the result of `iter` and returns each element as part of a
tuple instead. The first element of the tuple returned from `enumerate` is the
index, and the second element is a reference to the element. This is a bit more
convenient than calculating the index ourselves.

Because the `enumerate` method returns a tuple, we can use patterns to
destructure that tuple. We’ll be discussing patterns more in Chapter 6. In the
`for` loop, we specify a pattern that has `i` for the index in the tuple and
`&item` for the single byte in the tuple [2]. Because we get a reference to the
element from `.iter().enumerate()`, we use `&` in the pattern.

Inside the `for` loop, we search for the byte that represents the space by
using the byte literal syntax [4]. If we find a space, we return the position.
Otherwise, we return the length of the string by using `s.len()` [5].

We now have a way to find out the index of the end of the first word in the
string, but there’s a problem. We’re returning a `usize` on its own, but it’s
only a meaningful number in the context of the `&String`. In other words,
because it’s a separate value from the `String`, there’s no guarantee that it
will still be valid in the future. Consider the program in Listing 4-8 that
uses the `first_word` function from Listing 4-7.

```
// src/main.rs
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s); // word will get the value 5

    s.clear(); // this empties the String, making it equal to ""

    // word still has the value 5 here, but there's no more string that
    // we could meaningfully use the value 5 with. word is now totally invalid!
}
```

Listing 4-8: Storing the result from calling the `first_word` function and then
changing the `String` contents

This program compiles without any errors and would also do so if we used `word`
after calling `s.clear()`. Because `word` isn’t connected to the state of `s`
at all, `word` still contains the value `5`. We could use that value `5` with
the variable `s` to try to extract the first word out, but this would be a bug
because the contents of `s` have changed since we saved `5` in `word`.

Having to worry about the index in `word` getting out of sync with the data in
`s` is tedious and error prone! Managing these indices is even more brittle if
we write a `second_word` function. Its signature would have to look like this:

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Now we’re tracking a starting _and_ an ending index, and we have even more
values that were calculated from data in a particular state but aren’t tied to
that state at all. We have three unrelated variables floating around that need
to be kept in sync.

Luckily, Rust has a solution to this problem: string slices.
