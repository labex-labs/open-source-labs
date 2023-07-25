# Using the search Function in the run Function

Now that the `search` function is working and tested, we need to call `search`
from our `run` function. We need to pass the `config.query` value and the
`contents` that `run` reads from the file to the `search` function. Then `run`
will print each line returned from `search`:

Filename: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

We’re still using a `for` loop to return each line from `search` and print it.

Now the entire program should work! Let’s try it out, first with a word that
should return exactly one line from the Emily Dickinson poem: _frog_.

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

Cool! Now let’s try a word that will match multiple lines, like _body_:

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

And finally, let’s make sure that we don’t get any lines when we search for a
word that isn’t anywhere in the poem, such as _monomorphization_:

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

Excellent! We’ve built our own mini version of a classic tool and learned a lot
about how to structure applications. We’ve also learned a bit about file input
and output, lifetimes, testing, and command line parsing.

To round out this project, we’ll briefly demonstrate how to work with
environment variables and how to print to standard error, both of which are
useful when you’re writing command line programs.
