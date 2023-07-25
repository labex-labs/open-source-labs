# Default Implementations

Sometimes it’s useful to have default behavior for some or all of the methods
in a trait instead of requiring implementations for all methods on every type.
Then, as we implement the trait on a particular type, we can keep or override
each method’s default behavior.

In Listing 10-14, we specify a default string for the `summarize` method of the
`Summary` trait instead of only defining the method signature, as we did in
Listing 10-12.

Filename: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

Listing 10-14: Defining a `Summary` trait with a default implementation of the
`summarize` method

To use a default implementation to summarize instances of `NewsArticle`, we
specify an empty `impl` block with `impl Summary for NewsArticle {}`.

Even though we’re no longer defining the `summarize` method on `NewsArticle`
directly, we’ve provided a default implementation and specified that
`NewsArticle` implements the `Summary` trait. As a result, we can still call
the `summarize` method on an instance of `NewsArticle`, like this:

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

This code prints `New article available! (Read more...)`.

Creating a default implementation doesn’t require us to change anything about
the implementation of `Summary` on `Tweet` in Listing 10-13. The reason is that
the syntax for overriding a default implementation is the same as the syntax
for implementing a trait method that doesn’t have a default implementation.

Default implementations can call other methods in the same trait, even if those
other methods don’t have a default implementation. In this way, a trait can
provide a lot of useful functionality and only require implementors to specify
a small part of it. For example, we could define the `Summary` trait to have a
`summarize_author` method whose implementation is required, and then define a
`summarize` method that has a default implementation that calls the
`summarize_author` method:

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Read more from {}...)",
            self.summarize_author()
        )
    }
}
```

To use this version of `Summary`, we only need to define `summarize_author`
when we implement the trait on a type:

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

After we define `summarize_author`, we can call `summarize` on instances of the
`Tweet` struct, and the default implementation of `summarize` will call the
definition of `summarize_author` that we’ve provided. Because we’ve implemented
`summarize_author`, the `Summary` trait has given us the behavior of the
`summarize` method without requiring us to write any more code. Here’s what
that looks like:

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

This code prints `1 new tweet: (Read more from @horse_ebooks...)`.

Note that it isn’t possible to call the default implementation from an
overriding implementation of that same method.
