# Checking Where Errors Are Written

First let's observe how the content printed by `minigrep` is currently being written to standard output, including any error messages we want to write to standard error instead. We'll do that by redirecting the standard output stream to a file while intentionally causing an error. We won't redirect the standard error stream, so any content sent to standard error will continue to display on the screen.

Command line programs are expected to send error messages to the standard error stream so we can still see error messages on the screen even if we redirect the standard output stream to a file. Our program is not currently well behaved: we're about to see that it saves the error message output to a file instead!

To demonstrate this behavior, we'll run the program with `>` and the file path, _output.txt_, that we want to redirect the standard output stream to. We won't pass any arguments, which should cause an error:

```bash
cargo run > output.txt
```

The `>` syntax tells the shell to write the contents of standard output to _output.txt_ instead of the screen. We didn't see the error message we were expecting printed to the screen, so that means it must have ended up in the file. This is what _output.txt_ contains:

```rust
Problem parsing arguments: not enough arguments
```

Yup, our error message is being printed to standard output. It's much more useful for error messages like this to be printed to standard error so only data from a successful run ends up in the file. We'll change that.
