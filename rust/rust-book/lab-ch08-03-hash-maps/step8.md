# Updating a Value Based on the Old Value

Another common use case for hash maps is to look up a key’s value and then
update it based on the old value. For instance, Listing 8-25 shows code that
counts how many times each word appears in some text. We use a hash map with
the words as keys and increment the value to keep track of how many times we’ve
seen that word. If it’s the first time we’ve seen a word, we’ll first insert
the value `0`.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Listing 8-25: Counting occurrences of words using a hash map that stores words
and counts

This code will print `{"world": 2, "hello": 1, "wonderful": 1}`. You might see
the same key–value pairs printed in a different order: recall from “Accessing
Values in a Hash Map” on page XX that iterating over a hash map happens in an
arbitrary order.

The `split_whitespace` method returns an iterator over subslices, separated by
whitespace, of the value in `text`. The `or_insert` method returns a mutable
reference (`&mut V`) to the value for the specified key. Here, we store that
mutable reference in the `count` variable, so in order to assign to that value,
we must first dereference `count` using the asterisk (`*`). The mutable
reference goes out of scope at the end of the `for` loop, so all of these
changes are safe and allowed by the borrowing rules.
