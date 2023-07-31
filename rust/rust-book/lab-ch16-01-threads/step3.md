# Waiting for All Threads to Finish Using join Handles

The code in Listing 16-1 not only stops the spawned thread prematurely most of the time due to the main thread ending, but because there is no guarantee on the order in which threads run, we also can't guarantee that the spawned thread will get to run at all!

We can fix the problem of the spawned thread not running or of it ending prematurely by saving the return value of `thread::spawn` in a variable. The return type of `thread::spawn` is `JoinHandle<T>`. A `JoinHandle<T>` is an owned value that, when we call the `join` method on it, will wait for its thread to finish. Listing 16-2 shows how to use the `JoinHandle<T>` of the thread we created in Listing 16-1 and call `join` to make sure the spawned thread finishes before `main` exits.

Filename: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Listing 16-2: Saving a `JoinHandle<T>` from `thread::spawn` to guarantee the thread is run to completion

Calling `join` on the handle blocks the thread currently running until the thread represented by the handle terminates. _Blocking_ a thread means that thread is prevented from performing work or exiting. Because we've put the call to `join` after the main thread's `for` loop, running Listing 16-2 should produce output similar to this:

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

The two threads continue alternating, but the main thread waits because of the call to `handle.join()` and does not end until the spawned thread is finished.

But let's see what happens when we instead move `handle.join()` before the `for` loop in `main`, like this:

Filename: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

The main thread will wait for the spawned thread to finish and then run its `for` loop, so the output won't be interleaved anymore, as shown here:

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

Small details, such as where `join` is called, can affect whether or not your threads run at the same time.
