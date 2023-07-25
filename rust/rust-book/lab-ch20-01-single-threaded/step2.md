# Listening to the TCP Connection

Our web server needs to listen to a TCP connection, so that’s the first part
we’ll work on. The standard library offers a `std::net` module that lets us do
this. Let’s make a new project in the usual fashion:

```bash
$ cargo new hello
     Created binary (application) `hello` project
$ cd hello
```

Now enter the code in Listing 20-1 in `src/main.rs` to start. This code will
listen at the local address `127.0.0.1:7878` for incoming TCP streams. When it
gets an incoming stream, it will print `Connection established!`.

Filename: `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
  1 let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

  2 for stream in listener.incoming() {
      3 let stream = stream.unwrap();

      4 println!("Connection established!");
    }
}
```

Listing 20-1: Listening for incoming streams and printing a message when we
receive a stream

Using `TcpListener`, we can listen for TCP connections at the address
`127.0.0.1:7878` [1]. In the address, the section before the colon is an IP
address representing your computer (this is the same on every computer and
doesn’t represent the authors’ computer specifically), and `7878` is the port.
We’ve chosen this port for two reasons: HTTP isn’t normally accepted on this
port, so our server is unlikely to conflict with any other web server you might
have running on your machine, and 7878 is _rust_ typed on a telephone.

The `bind` function in this scenario works like the `new` function in that it
will return a new `TcpListener` instance. The function is called `bind`
because, in networking, connecting to a port to listen to is known as “binding
to a port.”

The `bind` function returns a `Result<T, E>`, which indicates that it’s
possible for binding to fail. For example, connecting to port 80 requires
administrator privileges (non-administrators can listen only on ports higher
than 1023), so if we tried to connect to port 80 without being an
administrator, binding wouldn’t work. Binding also wouldn’t work, for example,
if we ran two instances of our program and so had two programs listening to the
same port. Because we’re writing a basic server just for learning purposes, we
won’t worry about handling these kinds of errors; instead, we use `unwrap` to
stop the program if errors happen.

The `incoming` method on `TcpListener` returns an iterator that gives us a
sequence of streams [2] (more specifically, streams of type `TcpStream`). A
single _stream_ represents an open connection between the client and the
server. A _connection_ is the name for the full request and response process in
which a client connects to the server, the server generates a response, and the
server closes the connection. As such, we will read from the `TcpStream` to see
what the client sent and then write our response to the stream to send data
back to the client. Overall, this `for` loop will process each connection in
turn and produce a series of streams for us to handle.

For now, our handling of the stream consists of calling `unwrap` to terminate
our program if the stream has any errors [3]; if there aren’t any errors, the
program prints a message [4]. We’ll add more functionality for the success case
in the next listing. The reason we might receive errors from the `incoming`
method when a client connects to the server is that we’re not actually
iterating over connections. Instead, we’re iterating over _connection
attempts_. The connection might not be successful for a number of reasons, many
of them operating system specific. For example, many operating systems have a
limit to the number of simultaneous open connections they can support; new
connection attempts beyond that number will produce an error until some of the
open connections are closed.

Let’s try running this code! Invoke `cargo run` in the terminal and then load
_127.0.0.1:7878_ in a web browser. The browser should show an error message
like “Connection reset” because the server isn’t currently sending back any
data. But when you look at your terminal, you should see several messages that
were printed when the browser connected to the server!

```
     Running `target/debug/hello`
Connection established!
Connection established!
Connection established!
```

Sometimes you’ll see multiple messages printed for one browser request; the
reason might be that the browser is making a request for the page as well as a
request for other resources, like the _favicon.ico_ icon that appears in the
browser tab.

It could also be that the browser is trying to connect to the server multiple
times because the server isn’t responding with any data. When `stream` goes out
of scope and is dropped at the end of the loop, the connection is closed as
part of the `drop` implementation. Browsers sometimes deal with closed
connections by retrying, because the problem might be temporary. The important
factor is that we’ve successfully gotten a handle to a TCP connection!

Remember to stop the program by pressing ctrl-C when you’re done running a
particular version of the code. Then restart the program by invoking the `cargo
run` command after you’ve made each set of code changes to make sure you’re
running the newest code.
