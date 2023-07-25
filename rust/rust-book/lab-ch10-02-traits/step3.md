# Implementing a Trait on a Type

Now that we’ve defined the desired signatures of the `Summary` trait’s methods,
we can implement it on the types in our media aggregator. Listing 10-13 shows
an implementation of the `Summary` trait on the `NewsArticle` struct that uses
the headline, the author, and the location to create the return value of
`summarize`. For the `Tweet` struct, we define `summarize` as the username
followed by the entire text of the tweet, assuming that the tweet content is
already limited to 280 characters.

Filename: `src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

Listing 10-13: Implementing the `Summary` trait on the `NewsArticle` and
`Tweet` types

Implementing a trait on a type is similar to implementing regular methods. The
difference is that after `impl`, we put the trait name we want to implement,
then use the `for` keyword, and then specify the name of the type we want to
implement the trait for. Within the `impl` block, we put the method signatures
that the trait definition has defined. Instead of adding a semicolon after each
signature, we use curly brackets and fill in the method body with the specific
behavior that we want the methods of the trait to have for the particular type.

Now that the library has implemented the `Summary` trait on `NewsArticle` and
`Tweet`, users of the crate can call the trait methods on instances of
`NewsArticle` and `Tweet` in the same way we call regular methods. The only
difference is that the user must bring the trait into scope as well as the
types. Here’s an example of how a binary crate could use our `aggregator`
library crate:

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

This code prints `1 new tweet: horse_ebooks: of course, as you probably already
know, people`.

Other crates that depend on the `aggregator` crate can also bring the `Summary`
trait into scope to implement `Summary` on their own types. One restriction to
note is that we can implement a trait on a type only if either the trait or the
type, or both, are local to our crate. For example, we can implement standard
library traits like `Display` on a custom type like `Tweet` as part of our
`aggregator` crate functionality because the type `Tweet` is local to our
`aggregator` crate. We can also implement `Summary` on `Vec<T>` in our
`aggregator` crate because the trait `Summary` is local to our `aggregator`
crate.

But we can’t implement external traits on external types. For example, we can’t
implement the `Display` trait on `Vec<T>` within our `aggregator` crate because
`Display` and `Vec<T>` are both defined in the standard library and aren’t
local to our `aggregator` crate. This restriction is part of a property called
_coherence_, and more specifically the _orphan rule_, so named because the
parent type is not present. This rule ensures that other people’s code can’t
break your code and vice versa. Without the rule, two crates could implement
the same trait for the same type, and Rust wouldn’t know which implementation
to use.
