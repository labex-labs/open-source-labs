# Trade-offs of the State Pattern

We’ve shown that Rust is capable of implementing the object-oriented state
pattern to encapsulate the different kinds of behavior a post should have in
each state. The methods on `Post` know nothing about the various behaviors. The
way we organized the code, we have to look in only one place to know the
different ways a published post can behave: the implementation of the `State`
trait on the `Published` struct.

If we were to create an alternative implementation that didn’t use the state
pattern, we might instead use `match` expressions in the methods on `Post` or
even in the `main` code that checks the state of the post and changes behavior
in those places. That would mean we would have to look in several places to
understand all the implications of a post being in the published state! This
would only increase the more states we added: each of those `match` expressions
would need another arm.

With the state pattern, the `Post` methods and the places we use `Post` don’t
need `match` expressions, and to add a new state, we would only need to add a
new struct and implement the trait methods on that one struct.

The implementation using the state pattern is easy to extend to add more
functionality. To see the simplicity of maintaining code that uses the state
pattern, try a few of these suggestions:

- Add a `reject` method that changes the post’s state from `PendingReview` back
  to `Draft`.
- Require two calls to `approve` before the state can be changed to `Published`.
- Allow users to add text content only when a post is in the `Draft` state.
  Hint: have the state object responsible for what might change about the content
  but not responsible for modifying the `Post`.

One downside of the state pattern is that, because the states implement the
transitions between states, some of the states are coupled to each other. If we
add another state between `PendingReview` and `Published`, such as `Scheduled`,
we would have to change the code in `PendingReview` to transition to
`Scheduled` instead. It would be less work if `PendingReview` didn’t need to
change with the addition of a new state, but that would mean switching to
another design pattern.

Another downside is that we’ve duplicated some logic. To eliminate some of the
duplication, we might try to make default implementations for the
`request_review` and `approve` methods on the `State` trait that return `self`.
However, this wouldn’t work: when using `State` as a trait object, the trait
doesn’t know what the concrete `self` will be exactly, so the return type isn’t
known at compile time.

Other duplication includes the similar implementations of the `request_review`
and `approve` methods on `Post`. Both methods delegate to the implementation of
the same method on the value in the `state` field of `Option` and set the new
value of the `state` field to the result. If we had a lot of methods on `Post`
that followed this pattern, we might consider defining a macro to eliminate the
repetition (see “Macros” on page XX).

By implementing the state pattern exactly as it’s defined for object-oriented
languages, we’re not taking as full advantage of Rust’s strengths as we could.
Let’s look at some changes we can make to the `blog` crate that can make
invalid states and transitions into compile-time errors.
