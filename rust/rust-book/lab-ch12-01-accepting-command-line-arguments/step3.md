# Saving the Argument Values in Variables

The program is currently able to access the values specified as command line
arguments. Now we need to save the values of the two arguments in variables so
we can use the values throughout the rest of the program. We do that in Listing
12-2.

Filename: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Listing 12-2: Creating variables to hold the query argument and file path
argument

As we saw when we printed the vector, the program’s name takes up the first
value in the vector at `args[0]`, so we’re starting arguments at index 1. The
first argument `minigrep` takes is the string we’re searching for, so we put a
reference to the first argument in the variable `query`. The second argument
will be the file path, so we put a reference to the second argument in the
variable `file_path`.

We temporarily print the values of these variables to prove that the code is
working as we intend. Let’s run this program again with the arguments `test`
and `sample.txt`:

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Great, the program is working! The values of the arguments we need are being
saved into the right variables. Later we’ll add some error handling to deal
with certain potential erroneous situations, such as when the user provides no
arguments; for now, we’ll ignore that situation and work on adding file-reading
capabilities instead.
