# Sending Code from the ThreadPool to a Thread

We left a comment in the `for` loop in Listing 20-14 regarding the creation of
threads. Here, we’ll look at how we actually create threads. The standard
library provides `thread::spawn` as a way to create threads, and
`thread::spawn` expects to get some code the thread should run as soon as the
thread is created. However, in our case, we want to create the threads and have
them _wait_ for code that we’ll send later. The standard library’s
implementation of threads doesn’t include any way to do that; we have to
implement it manually.

We’ll implement this behavior by introducing a new data structure between the
`ThreadPool` and the threads that will manage this new behavior. We’ll call
this data structure _Worker_, which is a common term in pooling
implementations. The `Worker` picks up code that needs to be run and runs the
code in its thread.

Think of people working in the kitchen at a restaurant: the workers wait until
orders come in from customers, and then they’re responsible for taking those
orders and filling them.

Instead of storing a vector of `JoinHandle<()>` instances in the thread pool,
we’ll store instances of the `Worker` struct. Each `Worker` will store a single
`JoinHandle<()>` instance. Then we’ll implement a method on `Worker` that will
take a closure of code to run and send it to the already running thread for
execution. We’ll also give each `Worker` an `id` so we can distinguish between
the different instances of `Worker` in the pool when logging or debugging.

Here is the new process that will happen when we create a `ThreadPool`. We’ll
implement the code that sends the closure to the thread after we have `Worker`
set up in this way:

1. Define a `Worker` struct that holds an `id` and a `JoinHandle<()>`.
1. Change `ThreadPool` to hold a vector of `Worker` instances.
1. Define a `Worker::new` function that takes an `id` number and returns a
   `Worker` instance that holds the `id` and a thread spawned with an empty
   closure.
1. In `ThreadPool::new`, use the `for` loop counter to generate an `id`, create
   a new `Worker` with that `id`, and store the `Worker` in the vector.

If you’re up for a challenge, try implementing these changes on your own before
looking at the code in Listing 20-15.

Ready? Here is Listing 20-15 with one way to make the preceding modifications.

Filename: `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Listing 20-15: Modifying `ThreadPool` to hold `Worker` instances instead of
holding threads directly

We’ve changed the name of the field on `ThreadPool` from `threads` to `workers`
because it’s now holding `Worker` instances instead of `JoinHandle<()>`
instances [1]. We use the counter in the `for` loop [2] as an argument to
`Worker::new`, and we store each new `Worker` in the vector named `workers` [3].

External code (like our server in `src/main.rs`) doesn’t need to know the
implementation details regarding using a `Worker` struct within `ThreadPool`,
so we make the `Worker` struct [4] and its `new` function [5] private. The
`Worker::new` function uses the `id` we give it [7] and stores a
`JoinHandle<()>` instance [8] that is created by spawning a new thread using an
empty closure [6].

> Note: If the operating system can’t create a thread because there aren’t
> enough system resources, `thread::spawn` will panic. That will cause our whole
> server to panic, even though the creation of some threads might succeed. For
> simplicity’s sake, this behavior is fine, but in a production thread pool
> implementation, you’d likely want to use `std::thread::Builder` and its `spawn`
> method that returns `Result` instead.

This code will compile and will store the number of `Worker` instances we
specified as an argument to `ThreadPool::new`. But we’re _still_ not processing
the closure that we get in `execute`. Let’s look at how to do that next.
