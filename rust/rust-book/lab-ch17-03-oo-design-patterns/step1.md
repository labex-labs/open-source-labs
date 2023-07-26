# Implementing an Object-Oriented Design Pattern

The _state pattern_ is an object-oriented design pattern. The crux of the
pattern is that we define a set of states a value can have internally. The
states are represented by a set of _state objects_, and the value’s behavior
changes based on its state. We’re going to work through an example of a blog
post struct that has a field to hold its state, which will be a state object
from the set “draft,” “review,” or “published.”

The state objects share functionality: in Rust, of course, we use structs and
traits rather than objects and inheritance. Each state object is responsible
for its own behavior and for governing when it should change into another
state. The value that holds a state object knows nothing about the different
behavior of the states or when to transition between states.

The advantage of using the state pattern is that, when the business
requirements of the program change, we won’t need to change the code of the
value holding the state or the code that uses the value. We’ll only need to
update the code inside one of the state objects to change its rules or perhaps
add more state objects.

First we’re going to implement the state pattern in a more traditional
object-oriented way, then we’ll use an approach that’s a bit more natural in
Rust. Let’s dig in to incrementally implement a blog post workflow using the
state pattern.

The final functionality will look like this:

1. A blog post starts as an empty draft.
1. When the draft is done, a review of the post is requested.
1. When the post is approved, it gets published.
1. Only published blog posts return content to print, so unapproved posts can’t
   accidentally be published.

Any other changes attempted on a post should have no effect. For example, if we
try to approve a draft blog post before we’ve requested a review, the post
should remain an unpublished draft.

Listing 17-11 shows this workflow in code form: this is an example usage of the
API we’ll implement in a library crate named `blog`. This won’t compile yet
because we haven’t implemented the `blog` crate.

Filename: `src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-11: Code that demonstrates the desired behavior we want our `blog`
crate to have

We want to allow the user to create a new draft blog post with `Post::new` [1].
We want to allow text to be added to the blog post [2]. If we try to get the
post’s content immediately, before approval, we shouldn’t get any text because
the post is still a draft. We’ve added `assert_eq!` in the code for
demonstration purposes [3]. An excellent unit test for this would be to assert
that a draft blog post returns an empty string from the `content` method, but
we’re not going to write tests for this example.

Next, we want to enable a request for a review of the post [4], and we want
`content` to return an empty string while waiting for the review [5]. When the
post receives approval [6], it should get published, meaning the text of the
post will be returned when `content` is called [7].

Notice that the only type we’re interacting with from the crate is the `Post`
type. This type will use the state pattern and will hold a value that will be
one of three state objects representing the various states a post can be
in—draft, review, or published. Changing from one state to another will be
managed internally within the `Post` type. The states change in response to the
methods called by our library’s users on the `Post` instance, but they don’t
have to manage the state changes directly. Also, users can’t make a mistake
with the states, such as publishing a post before it’s reviewed.
