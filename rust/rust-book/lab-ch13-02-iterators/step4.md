# Methods That Produce Other Iterators

_Iterator adapters_ are methods defined on the `Iterator` trait that don’t
consume the iterator. Instead, they produce different iterators by changing
some aspect of the original iterator.

Listing 13-14 shows an example of calling the iterator adapter method `map`,
which takes a closure to call on each item as the items are iterated through.
The `map` method returns a new iterator that produces the modified items. The
closure here creates a new iterator in which each item from the vector will be
incremented by 1.

Filename: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

Listing 13-14: Calling the iterator adapter `map` to create a new iterator

However, this code produces a warning:

```
warning: unused `Map` that must be used
 --> src/main.rs:4:5
  |
4 |     v1.iter().map(|x| x + 1);
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_must_use)]` on by default
  = note: iterators are lazy and do nothing unless consumed
```

The code in Listing 13-14 doesn’t do anything; the closure we’ve specified
never gets called. The warning reminds us why: iterator adapters are lazy, and
we need to consume the iterator here.

To fix this warning and consume the iterator, we’ll use the `collect` method,
which we used with `env::args` in Listing 12-1. This method consumes the
iterator and collects the resultant values into a collection data type.

In Listing 13-15, we collect into a vector the results of iterating over the
iterator that’s returned from the call to `map`. This vector will end up
containing each item from the original vector, incremented by 1.

Filename: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

Listing 13-15: Calling the `map` method to create a new iterator, and then
calling the `collect` method to consume the new iterator and create a vector

Because `map` takes a closure, we can specify any operation we want to perform
on each item. This is a great example of how closures let you customize some
behavior while reusing the iteration behavior that the `Iterator` trait
provides.

You can chain multiple calls to iterator adapters to perform complex actions in
a readable way. But because all iterators are lazy, you have to call one of the
consuming adapter methods to get results from calls to iterator adapters.
