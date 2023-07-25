# Ignoring Some Tests Unless Specifically Requested

Sometimes a few specific tests can be very time-consuming to execute, so you
might want to exclude them during most runs of `cargo test`. Rather than
listing as arguments all tests you do want to run, you can instead annotate the
time-consuming tests using the `ignore` attribute to exclude them, as shown
here:

Filename: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // code that takes an hour to run
}
```

After `#[test]`, we add the `#[ignore]` line to the test we want to exclude.
Now when we run our tests, `it_works` runs, but `expensive_test` doesn’t:

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.60s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test expensive_test ... ignored
test it_works ... ok

test result: ok. 1 passed; 0 failed; 1 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

The `expensive_test` function is listed as `ignored`. If we want to run only
the ignored tests, we can use `cargo test -- --ignored`:

```bash
$ cargo test -- --ignored
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test expensive_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

By controlling which tests run, you can make sure your `cargo test` results
will be returned quickly. When you’re at a point where it makes sense to check
the results of the `ignored` tests and you have time to wait for the results,
you can run `cargo test -- --ignored` instead. If you want to run all tests
whether they’re ignored or not, you can run `cargo test -- --include-ignored`.
