# Reading a File

Now we’ll add functionality to read the file specified in the `file_path`
argument. First we need a sample file to test it with: we’ll use a file with a
small amount of text over multiple lines with some repeated words. Listing 12-3
has an Emily Dickinson poem that will work well! Create a file called
_poem.txt_ at the root level of your project, and enter the poem “I’m Nobody!
Who are you?”

Filename: poem.txt

```
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Listing 12-3: A poem by Emily Dickinson makes a good test case.

With the text in place, edit `src/main.rs` and add code to read the file, as
shown in Listing 12-4.

Filename: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listing 12-4: Reading the contents of the file specified by the second argument

First we bring in a relevant part of the standard library with a `use`
statement: we need `std::fs` to handle files [1].

In `main`, the new statement `fs::read_to_string` takes the `file_path`, opens
that file, and returns an `std::io::Result<String>` of the file’s contents [2].

After that, we again add a temporary `println!` statement that prints the value
of `contents` after the file is read, so we can check that the program is
working so far [3].

Let’s run this code with any string as the first command line argument (because
we haven’t implemented the searching part yet) and the _poem.txt_ file as the
second argument:

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Great! The code read and then printed the contents of the file. But the code
has a few flaws. At the moment, the `main` function has multiple
responsibilities: generally, functions are clearer and easier to maintain if
each function is responsible for only one idea. The other problem is that we’re
not handling errors as well as we could. The program is still small, so these
flaws aren’t a big problem, but as the program grows, it will be harder to fix
them cleanly. It’s a good practice to begin refactoring early on when
developing a program because it’s much easier to refactor smaller amounts of
code. We’ll do that next.
