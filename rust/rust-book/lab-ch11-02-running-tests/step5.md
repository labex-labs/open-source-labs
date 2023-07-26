# Running Single Tests

We can pass the name of any test function to `cargo test` to run only that test:

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

Only the test with the name `one_hundred` ran; the other two tests didn’t match
that name. The test output lets us know we had more tests that didn’t run by
displaying `2 filtered out` at the end.

We can’t specify the names of multiple tests in this way; only the first value
given to `cargo test` will be used. But there is a way to run multiple tests.
