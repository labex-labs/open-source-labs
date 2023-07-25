# How to Write Tests

Tests are Rust functions that verify that the non-test code is functioning in
the expected manner. The bodies of test functions typically perform these three
actions:

- Set up any needed data or state.
- Run the code you want to test.
- Assert that the results are what you expect.

Let’s look at the features Rust provides specifically for writing tests that
take these actions, which include the `test` attribute, a few macros, and the
`should_panic` attribute.
