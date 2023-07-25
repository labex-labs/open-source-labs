# Writing a Failing Test for the Case-Insensitive search Function

We first add a new `search_case_insensitive` function that will be called when
the environment variable has a value. We’ll continue to follow the TDD process,
so the first step is again to write a failing test. We’ll add a new test for
the new `search_case_insensitive` function and rename our old test from
`one_result` to `case_sensitive` to clarify the differences between the two
tests, as shown in Listing 12-20.

Filename: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Listing 12-20: Adding a new failing test for the case-insensitive function
we’re about to add

Note that we’ve edited the old test’s `contents` too. We’ve added a new line
with the text `"Duct tape."` using a capital _D_ that shouldn’t match the query
`"duct"` when we’re searching in a case-sensitive manner. Changing the old test
in this way helps ensure that we don’t accidentally break the case-sensitive
search functionality that we’ve already implemented. This test should pass now
and should continue to pass as we work on the case-insensitive search.

The new test for the case-_insensitive_ search uses `"rUsT"` as its query. In
the `search_case_insensitive` function we’re about to add, the query `"rUsT"`
should match the line containing `"Rust:"` with a capital _R_ and match the
line `"Trust me."` even though both have different casing from the query. This
is our failing test, and it will fail to compile because we haven’t yet defined
the `search_case_insensitive` function. Feel free to add a skeleton
implementation that always returns an empty vector, similar to the way we did
for the `search` function in Listing 12-16 to see the test compile and fail.
