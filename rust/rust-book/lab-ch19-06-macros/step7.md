# Function-like Macros

Function-like macros define macros that look like function calls. Similarly to
`macro_rules!` macros, they’re more flexible than functions; for example, they
can take an unknown number of arguments. However, `macro_rules!` macros can
only be defined using the match-like syntax we discussed in “Declarative Macros
with macro_rules! for General Metaprogramming” on page XX. Function-like macros
take a `TokenStream` parameter, and their definition manipulates that
`TokenStream` using Rust code as the other two types of procedural macros do.
An example of a function-like macro is an `sql!` macro that might be called
like so:

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

This macro would parse the SQL statement inside it and check that it’s
syntactically correct, which is much more complex processing than a
`macro_rules!` macro can do. The `sql!` macro would be defined like this:

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

This definition is similar to the custom `derive` macro’s signature: we receive
the tokens that are inside the parentheses and return the code we wanted to
generate.
