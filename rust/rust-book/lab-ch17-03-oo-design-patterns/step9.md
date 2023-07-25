# Implementing Transitions as Transformations into Different Types

So how do we get a published post? We want to enforce the rule that a draft
post has to be reviewed and approved before it can be published. A post in the
pending review state should still not display any content. Let’s implement
these constraints by adding another struct, `PendingReviewPost`, defining the
`request_review` method on `DraftPost` to return a `PendingReviewPost` and
defining an `approve` method on `PendingReviewPost` to return a `Post`, as
shown in Listing 17-20.

Filename: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Listing 17-20: A `PendingReviewPost` that gets created by calling
`request_review` on `DraftPost` and an `approve` method that turns a
`PendingReviewPost` into a published `Post`

The `request_review` and `approve` methods take ownership of `self`, thus
consuming the `DraftPost` and `PendingReviewPost` instances and transforming
them into a `PendingReviewPost` and a published `Post`, respectively. This way,
we won’t have any lingering `DraftPost` instances after we’ve called
`request_review` on them, and so forth. The `PendingReviewPost` struct doesn’t
have a `content` method defined on it, so attempting to read its content
results in a compiler error, as with `DraftPost`. Because the only way to get a
published `Post` instance that does have a `content` method defined is to call
the `approve` method on a `PendingReviewPost`, and the only way to get a
`PendingReviewPost` is to call the `request_review` method on a `DraftPost`,
we’ve now encoded the blog post workflow into the type system.

But we also have to make some small changes to `main`. The `request_review` and
`approve` methods return new instances rather than modifying the struct they’re
called on, so we need to add more `let post =` shadowing assignments to save
the returned instances. We also can’t have the assertions about the draft and
pending review posts’ contents be empty strings, nor do we need them: we can’t
compile code that tries to use the content of posts in those states any longer.
The updated code in `main` is shown in Listing 17-21.

Filename: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-21: Modifications to `main` to use the new implementation of the
blog post workflow

The changes we needed to make to `main` to reassign `post` mean that this
implementation doesn’t quite follow the object-oriented state pattern anymore:
the transformations between the states are no longer encapsulated entirely
within the `Post` implementation. However, our gain is that invalid states are
now impossible because of the type system and the type checking that happens at
compile time! This ensures that certain bugs, such as display of the content of
an unpublished post, will be discovered before they make it to production.

Try the tasks suggested at the start of this section on the `blog` crate as it
is after Listing 17-21 to see what you think about the design of this version
of the code. Note that some of the tasks might be completed already in this
design.

We’ve seen that even though Rust is capable of implementing object-oriented
design patterns, other patterns, such as encoding state into the type system,
are also available in Rust. These patterns have different trade-offs. Although
you might be very familiar with object-oriented patterns, rethinking the
problem to take advantage of Rust’s features can provide benefits, such as
preventing some bugs at compile time. Object-oriented patterns won’t always be
the best solution in Rust due to certain features, like ownership, that
object-oriented languages don’t have.
