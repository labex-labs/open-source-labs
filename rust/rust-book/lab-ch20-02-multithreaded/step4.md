# Spawning a Thread for Each Request

First, let’s explore how our code might look if it did create a new thread for
every connection. As mentioned earlier, this isn’t our final plan due to the
problems with potentially spawning an unlimited number of threads, but it is a
starting point to get a working multithreaded server first. Then we’ll add the
thread pool as an improvement, and contrasting the two solutions will be easier.

Listing 20-11 shows the changes to make to `main` to spawn a new thread to
handle each stream within the `for` loop.

Filename: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-11: Spawning a new thread for each stream

As you learned in Chapter 16, `thread::spawn` will create a new thread and then
run the code in the closure in the new thread. If you run this code and load
_/sleep_ in your browser, then _/_ in two more browser tabs, you’ll indeed see
that the requests to _/_ don’t have to wait for _/sleep_ to finish. However, as
we mentioned, this will eventually overwhelm the system because you’d be making
new threads without any limit.

#
