# Validating the Request and Selectively Responding

Right now, our web server will return the HTML in the file no matter what the
client requested. Let’s add functionality to check that the browser is
requesting _/_ before returning the HTML file, and return an error if the
browser requests anything else. For this we need to modify `handle_connection`,
as shown in Listing 20-6. This new code checks the content of the request
received against what we know a request for _/_ looks like and adds `if` and
`else` blocks to treat requests differently.

Filename: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
        .lines()
        .next()
        .unwrap()
        .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // some other request
    }
}
```

Listing 20-6: Handling requests to _/_ differently from other requests

We’re only going to be looking at the first line of the HTTP request, so rather
than reading the entire request into a vector, we’re calling `next` to get the
first item from the iterator [1]. The first `unwrap` takes care of the `Option`
and stops the program if the iterator has no items. The second `unwrap` handles
the `Result` and has the same effect as the `unwrap` that was in the `map`
added in Listing 20-2.

Next, we check the `request_line` to see if it equals the request line of a GET
request to the _/_ path [2]. If it does, the `if` block returns the contents of
our HTML file.

If the `request_line` does _not_ equal the GET request to the _/_ path, it
means we’ve received some other request. We’ll add code to the `else` block [3]
in a moment to respond to all other requests.

Run this code now and request _127.0.0.1:7878_; you should get the HTML in
_hello.html_. If you make any other request, such as
_127.0.0.1:7878/something-else_, you’ll get a connection error like those you
saw when running the code in Listing 20-1 and Listing 20-2.

Now let’s add the code in Listing 20-7 to the `else` block to return a response
with the status code 404, which signals that the content for the request was
not found. We’ll also return some HTML for a page to render in the browser
indicating the response to the end user.

Filename: `src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listing 20-7: Responding with status code 404 and an error page if anything
other than _/_ was requested

Here, our response has a status line with status code 404 and the reason phrase
`NOT FOUND` [1]. The body of the response will be the HTML in the file
_404.html_ [1]. You’ll need to create a _404.html_ file next to _hello.html_
for the error page; again feel free to use any HTML you want, or use the
example HTML in Listing 20-8.

Filename: `404.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Oops!</h1>
    <p>Sorry, I don't know what you're asking for.</p>
  </body>
</html>
```

Listing 20-8: Sample content for the page to send back with any 404 response

With these changes, run your server again. Requesting _127.0.0.1:7878_ should
return the contents of _hello.html_, and any other request, like
_127.0.0.1:7878/foo_, should return the error HTML from _404.html_.
