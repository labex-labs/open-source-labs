# Encoding States and Behavior as Types

We’ll show you how to rethink the state pattern to get a different set of
trade-offs. Rather than encapsulating the states and transitions completely so
outside code has no knowledge of them, we’ll encode the states into different
types. Consequently, Rust’s type checking system will prevent attempts to use
draft posts where only published posts are allowed by issuing a compiler error.

Let’s consider the first part of `main` in Listing 17-11:

Filename: `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

We still enable the creation of new posts in the draft state using `Post::new`
and the ability to add text to the post’s content. But instead of having a
`content` method on a draft post that returns an empty string, we’ll make it so
draft posts don’t have the `content` method at all. That way, if we try to get
a draft post’s content, we’ll get a compiler error telling us the method
doesn’t exist. As a result, it will be impossible for us to accidentally
display draft post content in production because that code won’t even compile.
Listing 17-19 shows the definition of a `Post` struct and a `DraftPost` struct,
as well as methods on each.

Filename: `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-19: A `Post` with a `content` method and a `DraftPost` without a
`content` method

Both the `Post` and `DraftPost` structs have a private `content` field that
stores the blog post text. The structs no longer have the `state` field because
we’re moving the encoding of the state to the types of the structs. The `Post`
struct will represent a published post, and it has a `content` method that
returns the `content` [2].

We still have a `Post::new` function, but instead of returning an instance of
`Post`, it returns an instance of `DraftPost` [1]. Because `content` is private
and there aren’t any functions that return `Post`, it’s not possible to create
an instance of `Post` right now.

The `DraftPost` struct has an `add_text` method, so we can add text to
`content` as before [3], but note that `DraftPost` does not have a `content`
method defined! So now the program ensures all posts start as draft posts, and
draft posts don’t have their content available for display. Any attempt to get
around these constraints will result in a compiler error.

#
