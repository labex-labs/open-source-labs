# Defining Post and Creating a New Instance in the Draft State

Let’s get started on the implementation of the library! We know we need a
public `Post` struct that holds some content, so we’ll start with the
definition of the struct and an associated public `new` function to create an
instance of `Post`, as shown in Listing 17-12. We’ll also make a private
`State` trait that will define the behavior that all state objects for a `Post`
must have.

Then `Post` will hold a trait object of `Box<dyn State>` inside an `Option<T>`
in a private field named `state` to hold the state object. You’ll see why the
`Option<T>` is necessary in a bit.

Filename: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Listing 17-12: Definition of a `Post` struct and a `new` function that creates
a new `Post` instance, a `State` trait, and a `Draft` struct

The `State` trait defines the behavior shared by different post states. The
state objects are `Draft`, `PendingReview`, and `Published`, and they will all
implement the `State` trait. For now, the trait doesn’t have any methods, and
we’ll start by defining just the `Draft` state because that is the state we
want a post to start in.

When we create a new `Post`, we set its `state` field to a `Some` value that
holds a `Box` [1]. This `Box` points to a new instance of the `Draft` struct.
This ensures that whenever we create a new instance of `Post`, it will start
out as a draft. Because the `state` field of `Post` is private, there is no way
to create a `Post` in any other state! In the `Post::new` function, we set the
`content` field to a new, empty `String` [2].
