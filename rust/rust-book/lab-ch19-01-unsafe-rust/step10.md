# When to Use Unsafe Code

Using `unsafe` to use one of the five superpowers just discussed isn’t wrong or
even frowned upon, but it is trickier to get `unsafe` code correct because the
compiler can’t help uphold memory safety. When you have a reason to use
`unsafe` code, you can do so, and having the explicit `unsafe` annotation makes
it easier to track down the source of problems when they occur.
