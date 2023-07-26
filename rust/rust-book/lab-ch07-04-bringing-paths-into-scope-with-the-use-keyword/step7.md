# The Glob Operator

If we want to bring _all_ public items defined in a path into scope, we can specify that path followed by the `*` glob operator:

```rust
use std::collections::*;
```

This `use` statement brings all public items defined in `std::collections` into the current scope. Be careful when using the glob operator! Glob can make it harder to tell what names are in scope and where a name used in your program was defined.

The glob operator is often used when testing to bring everything under test into the `tests` module; we'll talk about that in "How to Write Tests" on page XX. The glob operator is also sometimes used as part of the prelude pattern: see the standard library documentation for more information on that pattern.
