# Submodules in Integration Tests

As you add more integration tests, you might want to make more files in the
`tests` directory to help organize them; for example, you can group the test
functions by the functionality they’re testing. As mentioned earlier, each file
in the `tests` directory is compiled as its own separate crate, which is useful
for creating separate scopes to more closely imitate the way end users will be
using your crate. However, this means files in the `tests` directory don’t
share the same behavior as files in `src` do, as you learned in Chapter 7
regarding how to separate code into modules and files.

The different behavior of `tests` directory files is most noticeable when you
have a set of helper functions to use in multiple integration test files and
you try to follow the steps in “Separating Modules into Different Files” on
page XX to extract them into a common module. For example, if we create
`tests/common.rs` and place a function named `setup` in it, we can add some
code to `setup` that we want to call from multiple test functions in multiple
test files:

Filename: `tests/common.rs`

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

When we run the tests again, we’ll see a new section in the test output for the
`common.rs` file, even though this file doesn’t contain any test functions nor
did we call the `setup` function from anywhere:

```
running 1 test
test tests::internal ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

     Running tests/common.rs (target/debug/deps/common-
92948b65e88960b4)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

     Running tests/integration_test.rs
(target/debug/deps/integration_test-92948b65e88960b4)

running 1 test
test it_adds_two ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

   Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

Having `common` appear in the test results with `running 0 tests` displayed for
it is not what we wanted. We just wanted to share some code with the other
integration test files. To avoid having `common` appear in the test output,
instead of creating `tests/common.rs`, we’ll create `_tests/common/mod.rs`. The
project directory now looks like this:

```
├── Cargo.lock
├── Cargo.toml
├── src
│   └── lib.rs
└── tests
    ├── common
    │   └── mod.rs
    └── integration_test.rs
```

This is the older naming convention that Rust also understands that we
mentioned in “Alternate File Paths” on page XX. Naming the file this way tells
Rust not to treat the `common` module as an integration test file. When we move
the `setup` function code into `tests/common/mod.rs` and delete the
`tests/common.rs` file, the section in the test output will no longer appear.
Files in subdirectories of the `tests` directory don’t get compiled as separate
crates or have sections in the test output.

After we’ve created `tests/common/mod.rs`, we can use it from any of the
integration test files as a module. Here’s an example of calling the `setup`
function from the `it_adds_two` test in \_tests/integration`test.rs`:

Filename: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

Note that the `mod common;` declaration is the same as the module declaration
we demonstrated in Listing 7-21. Then, in the test function, we can call the
`common::setup()` function.

#
