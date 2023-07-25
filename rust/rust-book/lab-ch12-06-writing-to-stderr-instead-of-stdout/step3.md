# Printing Errors to Standard Error

We’ll use the code in Listing 12-24 to change how error messages are printed.
Because of the refactoring we did earlier in this chapter, all the code that
prints error messages is in one function, `main`. The standard library provides
the `eprintln!` macro that prints to the standard error stream, so let’s change
the two places we were calling `println!` to print errors to use `eprintln!`
instead.

Filename: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Listing 12-24: Writing error messages to standard error instead of standard
output using `eprintln!`

Let’s now run the program again in the same way, without any arguments and
redirecting standard output with `>`:

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

Now we see the error onscreen and _output.txt_ contains nothing, which is the
behavior we expect of command line programs.

Let’s run the program again with arguments that don’t cause an error but still
redirect standard output to a file, like so:

```bash
cargo run -- to poem.txt > output.txt
```

We won’t see any output to the terminal, and _output.txt_ will contain our
results:

Filename: output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

This demonstrates that we’re now using standard output for successful output
and standard error for error output as appropriate.
