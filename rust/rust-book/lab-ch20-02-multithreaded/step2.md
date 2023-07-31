# Simulating a Slow Request

We'll look at how a slow-processing request can affect other requests made to our current server implementation. Listing 20-10 implements handling a request to _/sleep_ with a simulated slow response that will cause the server to sleep for five seconds before responding.

Filename: `src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

Listing 20-10: Simulating a slow request by sleeping for five seconds

We switched from `if` to `match` now that we have three cases \[1\]. We need to explicitly match on a slice of `request_line` to pattern-match against the string literal values; `match` doesn't do automatic referencing and dereferencing, like the equality method does.

The first arm \[2\] is the same as the `if` block from Listing 20-9. The second arm \[3\] matches a request to _/sleep_. When that request is received, the server will sleep for five seconds before rendering the successful HTML page. The third arm \[4\] is the same as the `else` block from Listing 20-9.

You can see how primitive our server is: real libraries would handle the recognition of multiple requests in a much less verbose way!

Start the server using `cargo run`. Then open two browser windows: one for *http://127.0.0.1:7878* and the other for *http://127.0.0.1:7878/sleep*. If you enter the _/_ URI a few times, as before, you'll see it respond quickly. But if you enter _/sleep_ and then load _/_, you'll see that _/_ waits until `sleep` has slept for its full five seconds before loading.

There are multiple techniques we could use to avoid requests backing up behind a slow request; the one we'll implement is a thread pool.
