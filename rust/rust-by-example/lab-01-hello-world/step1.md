# Hello World

This is the source code of the traditional Hello World program.

```rust
// This is a comment, and is ignored by the compiler.
// This is the main function.
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");
}
```

`println!` is a _macro_ that prints text to the console.

A binary can be generated using the Rust compiler: `rustc`.

```bash
rustc hello.rs
```

`rustc` will produce a `hello` binary that can be executed.

```bash
$ ./hello
Hello World!
```

## Activity

Run above to see the expected output. Next, add a new line with a second `println!` macro so that the output shows:

```text
Hello World!
I'm a Rustacean!
```
