# Running Tests in Parallel or Consecutively

When you run multiple tests, by default they run in parallel using threads,
meaning they finish running faster and you get feedback quicker. Because the
tests are running at the same time, you must make sure your tests don’t depend
on each other or on any shared state, including a shared environment, such as
the current working directory or environment variables.

For example, say each of your tests runs some code that creates a file on disk
named _test-output.txt_ and writes some data to that file. Then each test reads
the data in that file and asserts that the file contains a particular value,
which is different in each test. Because the tests run at the same time, one
test might overwrite the file in the time between another test writing and
reading the file. The second test will then fail, not because the code is
incorrect but because the tests have interfered with each other while running
in parallel. One solution is to make sure each test writes to a different file;
another solution is to run the tests one at a time.

If you don’t want to run the tests in parallel or if you want more fine-grained
control over the number of threads used, you can send the `--test-threads` flag
and the number of threads you want to use to the test binary. Take a look at
the following example:

```bash
cargo test -- --test-threads=1
```

We set the number of test threads to `1`, telling the program not to use any
parallelism. Running the tests using one thread will take longer than running
them in parallel, but the tests won’t interfere with each other if they share
state.
