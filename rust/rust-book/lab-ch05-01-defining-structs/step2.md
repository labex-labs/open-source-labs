# Using the Field Init Shorthand

Because the parameter names and the struct field names are exactly the same in
Listing 5-4, we can use the _field init shorthand_ syntax to rewrite
`build_user` so it behaves exactly the same but doesn’t have the repetition of
`username` and `email`, as shown in Listing 5-5.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Listing 5-5: A `build_user` function that uses field init shorthand because the
`username` and `email` parameters have the same name as struct fields

Here, we’re creating a new instance of the `User` struct, which has a field
named `email`. We want to set the `email` field’s value to the value in the
`email` parameter of the `build_user` function. Because the `email` field and
the `email` parameter have the same name, we only need to write `email` rather
than `email: email`.
