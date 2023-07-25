# Grouping Configuration Values

We can take another small step to improve the `parse_config` function further.
At the moment, we’re returning a tuple, but then we immediately break that
tuple into individual parts again. This is a sign that perhaps we don’t have
the right abstraction yet.

Another indicator that shows there’s room for improvement is the `config` part
of `parse_config`, which implies that the two values we return are related and
are both part of one configuration value. We’re not currently conveying this
meaning in the structure of the data other than by grouping the two values into
a tuple; we’ll instead put the two values into one struct and give each of the
struct fields a meaningful name. Doing so will make it easier for future
maintainers of this code to understand how the different values relate to each
other and what their purpose is.

Listing 12-6 shows the improvements to the `parse_config` function.

Filename: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
        .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

Listing 12-6: Refactoring `parse_config` to return an instance of a `Config`
struct

We’ve added a struct named `Config` defined to have fields named `query` and
`file_path` [5]. The signature of `parse_config` now indicates that it returns
a `Config` value [6]. In the body of `parse_config`, where we used to return
string slices that reference `String` values in `args`, we now define `Config`
to contain owned `String` values. The `args` variable in `main` is the owner of
the argument values and is only letting the `parse_config` function borrow
them, which means we’d violate Rust’s borrowing rules if `Config` tried to take
ownership of the values in `args`.

There are a number of ways we could manage the `String` data; the easiest,
though somewhat inefficient, route is to call the `clone` method on the values
[7] [8]. This will make a full copy of the data for the `Config` instance to
own, which takes more time and memory than storing a reference to the string
data. However, cloning the data also makes our code very straightforward
because we don’t have to manage the lifetimes of the references; in this
circumstance, giving up a little performance to gain simplicity is a worthwhile
trade-off.

> **The Trade-Offs of Using clone**
>
> There’s a tendency among many Rustaceans to avoid using `clone` to fix
> ownership problems because of its runtime cost. In Chapter 13, you’ll learn how
> to use more efficient methods in this type of situation. But for now, it’s okay
> to copy a few strings to continue making progress because you’ll make these
> copies only once and your file path and query string are very small. It’s
> better to have a working program that’s a bit inefficient than to try to
> hyperoptimize code on your first pass. As you become more experienced with
> Rust, it’ll be easier to start with the most efficient solution, but for now,
> it’s perfectly acceptable to call `clone`.

We’ve updated `main` so it places the instance of `Config` returned by
`parse_config` into a variable named `config` [1], and we updated the code that
previously used the separate `query` and `file_path` variables so it now uses
the fields on the `Config` struct instead [2] [3] [4].

Now our code more clearly conveys that `query` and `file_path` are related and
that their purpose is to configure how the program will work. Any code that
uses these values knows to find them in the `config` instance in the fields
named for their purpose.

#
