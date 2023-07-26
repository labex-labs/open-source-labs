# Creating Space to Store the Threads

Now that we have a way to know we have a valid number of threads to store in
the pool, we can create those threads and store them in the `ThreadPool` struct
before returning the struct. But how do we “store” a thread? Let’s take another
look at the `thread::spawn` signature:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

The `spawn` function returns a `JoinHandle<T>`, where `T` is the type that the
closure returns. Let’s try using `JoinHandle` too and see what happens. In our
case, the closures we’re passing to the thread pool will handle the connection
and not return anything, so `T` will be the unit type `()`.

The code in Listing 20-14 will compile but doesn’t create any threads yet.
We’ve changed the definition of `ThreadPool` to hold a vector of
`thread::JoinHandle<()>` instances, initialized the vector with a capacity of
`size`, set up a `for` loop that will run some code to create the threads, and
returned a `ThreadPool` instance containing them.

Filename: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Listing 20-14: Creating a vector for `ThreadPool` to hold the threads

We’ve brought `std::thread` into scope in the library crate [1] because we’re
using `thread::JoinHandle` as the type of the items in the vector in
`ThreadPool` [2].

Once a valid size is received, our `ThreadPool` creates a new vector that can
hold `size` items [3]. The `with_capacity` function performs the same task as
`Vec::new` but with an important difference: it pre-allocates space in the
vector. Because we know we need to store `size` elements in the vector, doing
this allocation up front is slightly more efficient than using `Vec::new`,
which resizes itself as elements are inserted.

When you run `cargo check` again, it should succeed.
