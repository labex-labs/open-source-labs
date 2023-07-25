# Validating References with Lifetimes

Lifetimes are another kind of generic that we’ve already been using. Rather
than ensuring that a type has the behavior we want, lifetimes ensure that
references are valid as long as we need them to be.

One detail we didn’t discuss in “References and Borrowing” on page XX is that
every reference in Rust has a _lifetime_, which is the scope for which that
reference is valid. Most of the time, lifetimes are implicit and inferred, just
like most of the time, types are inferred. We must annotate types only when
multiple types are possible. In a similar way, we must annotate lifetimes when
the lifetimes of references could be related in a few different ways. Rust
requires us to annotate the relationships using generic lifetime parameters to
ensure the actual references used at runtime will definitely be valid.

Annotating lifetimes is not even a concept most other programming languages
have, so this is going to feel unfamiliar. Although we won’t cover lifetimes in
their entirety in this chapter, we’ll discuss common ways you might encounter
lifetime syntax so you can get comfortable with the concept.
