# Multiple Ownership with Multiple Threads

In Chapter 15, we gave a value to multiple owners by using the smart pointer `Rc<T>` to create a reference counted value. Let's do the same here and see what happens. We'll wrap the `Mutex<T>` in `Rc<T>` in Listing 16-14 and clone the `Rc<T>` before moving ownership to the thread.

Filename: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-14: Attempting to use `Rc<T>` to allow multiple threads to own the `Mutex<T>`

Once again, we compile and get... different errors! The compiler is teaching us a lot.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

Wow, that error message is very wordy! Here's the important part to focus on: `` Rc<Mutex<i32>>` cannot be sent between threads safely` [1]. The compiler is also telling us the reason why: `the trait `Send` is not implemented for `Rc<Mutex<i32>> `` \[2\]. We'll talk about `Send` in the next section: it's one of the traits that ensures the types we use with threads are meant for use in concurrent situations.

Unfortunately, `Rc<T>` is not safe to share across threads. When `Rc<T>` manages the reference count, it adds to the count for each call to `clone` and subtracts from the count when each clone is dropped. But it doesn't use any concurrency primitives to make sure that changes to the count can't be interrupted by another thread. This could lead to wrong counts---subtle bugs that could in turn lead to memory leaks or a value being dropped before we're done with it. What we need is a type exactly like `Rc<T>` but one that makes changes to the reference count in a thread-safe way.
