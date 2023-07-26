# Validating the Number of Threads in new

We aren’t doing anything with the parameters to `new` and `execute`. Let’s
implement the bodies of these functions with the behavior we want. To start,
let’s think about `new`. Earlier we chose an unsigned type for the `size`
parameter because a pool with a negative number of threads makes no sense.
However, a pool with zero threads also makes no sense, yet zero is a perfectly
valid `usize`. We’ll add code to check that `size` is greater than zero before
we return a `ThreadPool` instance and have the program panic if it receives a
zero by using the `assert!` macro, as shown in Listing 20-13.

Filename: `src/lib.rs`

```rust
impl ThreadPool {
    /// Create a new ThreadPool.
    ///
    /// The size is the number of threads in the pool.
    ///
  1 /// # Panics
    ///
    /// The `new` function will panic if the size is zero.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Listing 20-13: Implementing `ThreadPool::new` to panic if `size` is zero

We’ve also added some documentation for our `ThreadPool` with doc comments.
Note that we followed good documentation practices by adding a section that
calls out the situations in which our function can panic [1], as discussed in
Chapter 14. Try running `cargo doc --open` and clicking the `ThreadPool` struct
to see what the generated docs for `new` look like!

Instead of adding the `assert!` macro as we’ve done here [2], we could change
`new` into `build` and return a `Result` like we did with `Config::build` in
the I/O project in Listing 12-9. But we’ve decided in this case that trying to
create a thread pool without any threads should be an unrecoverable error. If
you’re feeling ambitious, try to write a function named `build` with the
following signature to compare with the `new` function:

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```

#
