# Sending Multiple Values and Seeing the Receiver Waiting

The code in Listing 16-8 compiled and ran, but it didn’t clearly show us that
two separate threads were talking to each other over the channel. In Listing
16-10 we’ve made some modifications that will prove the code in Listing 16-8 is
running concurrently: the spawned thread will now send multiple messages and
pause for a second between each message.

Filename: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Listing 16-10: Sending multiple messages and pausing between each one

This time, the spawned thread has a vector of strings that we want to send to
the main thread. We iterate over them, sending each individually, and pause
between each by calling the `thread::sleep` function with a `Duration` value of
one second.

In the main thread, we’re not calling the `recv` function explicitly anymore:
instead, we’re treating `rx` as an iterator. For each value received, we’re
printing it. When the channel is closed, iteration will end.

When running the code in Listing 16-10, you should see the following output
with a one-second pause in between each line:

```
Got: hi
Got: from
Got: the
Got: thread
```

Because we don’t have any code that pauses or delays in the `for` loop in the
main thread, we can tell that the main thread is waiting to receive values from
the spawned thread.
