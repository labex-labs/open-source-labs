# Implementing the search_case_insensitive Function

The `search_case_insensitive` function, shown in Listing 12-21, will be almost
the same as the `search` function. The only difference is that we’ll lowercase
the `query` and each `line` so that whatever the case of the input arguments,
they’ll be the same case when we check whether the line contains the query.

Filename: `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Listing 12-21: Defining the `search_case_insensitive` function to lowercase the
query and the line before comparing them

First we lowercase the `query` string and store it in a shadowed variable with
the same name [1]. Calling `to_lowercase` on the query is necessary so that no
matter whether the user’s query is `"rust"`, `"RUST"`, `"Rust"`, or `"rUsT"`,
we’ll treat the query as if it were `"rust"` and be insensitive to the case.
While `to_lowercase` will handle basic Unicode, it won’t be 100% accurate. If
we were writing a real application, we’d want to do a bit more work here, but
this section is about environment variables, not Unicode, so we’ll leave it at
that here.

Note that `query` is now a `String` rather than a string slice because calling
`to_lowercase` creates new data rather than referencing existing data. Say the
query is `"rUsT"`, as an example: that string slice doesn’t contain a lowercase
`u` or `t` for us to use, so we have to allocate a new `String` containing
`"rust"`. When we pass `query` as an argument to the `contains` method now, we
need to add an ampersand [3] because the signature of `contains` is defined to
take a string slice.

Next, we add a call to `to_lowercase` on each `line` to lowercase all
characters [2]. Now that we’ve converted `line` and `query` to lowercase, we’ll
find matches no matter what the case of the query is.

Let’s see if this implementation passes the tests:

```
running 2 tests
test tests::case_insensitive ... ok
test tests::case_sensitive ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

Great! They passed. Now, let’s call the new `search_case_insensitive` function
from the `run` function. First we’ll add a configuration option to the `Config`
struct to switch between case-sensitive and case-insensitive search. Adding
this field will cause compiler errors because we aren’t initializing this field
anywhere yet:

Filename: `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

We added the `ignore_case` field that holds a Boolean. Next, we need the `run`
function to check the `ignore_case` field’s value and use that to decide
whether to call the `search` function or the `search_case_insensitive`
function, as shown in Listing 12-22. This still won’t compile yet.

Filename: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Listing 12-22: Calling either `search` or `search_case_insensitive` based on
the value in `config.ignore_case`

Finally, we need to check for the environment variable. The functions for
working with environment variables are in the `env` module in the standard
library, so we bring that module into scope at the top of `src/lib.rs`. Then
we’ll use the `var` function from the `env` module to check to see if any value
has been set for an environment variable named `IGNORE_CASE`, as shown in
Listing 12-23.

Filename: `src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 12-23: Checking for any value in an environment variable named
`IGNORE_CASE`

Here, we create a new variable, `ignore_case`. To set its value, we call the
`env::var` function and pass it the name of the `IGNORE_CASE` environment
variable. The `env::var` function returns a `Result` that will be the
successful `Ok` variant that contains the value of the environment variable if
the environment variable is set to any value. It will return the `Err` variant
if the environment variable is not set.

We’re using the `is_ok` method on the `Result` to check whether the environment
variable is set, which means the program should do a case-insensitive search.
If the `IGNORE_CASE` environment variable isn’t set to anything, `is_ok` will
return `false` and the program will perform a case-sensitive search. We don’t
care about the _value_ of the environment variable, just whether it’s set or
unset, so we’re checking `is_ok` rather than using `unwrap`, `expect`, or any
of the other methods we’ve seen on `Result`.

We pass the value in the `ignore_case` variable to the `Config` instance so the
`run` function can read that value and decide whether to call
`search_case_insensitive` or `search`, as we implemented in Listing 12-22.

Let’s give it a try! First we’ll run our program without the environment
variable set and with the query `to`, which should match any line that contains
the word _to_ in all lowercase:

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

Looks like that still works! Now let’s run the program with `IGNORE_CASE` set
to `1` but with the same query `to`:

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

If you’re using PowerShell, you will need to set the environment variable and
run the program as separate commands:

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

This will make `IGNORE_CASE` persist for the remainder of your shell session.
It can be unset with the `Remove-Item` cmdlet:

```rust
PS> Remove-Item Env:IGNORE_CASE
```

We should get lines that contain _to_ that might have uppercase letters:

```
Are you nobody, too?
How dreary to be somebody!
To tell your name the livelong day
To an admiring bog!
```

Excellent, we also got lines containing _To_! Our `minigrep` program can now do
case-insensitive searching controlled by an environment variable. Now you know
how to manage options set using either command line arguments or environment
variables.

Some programs allow arguments _and_ environment variables for the same
configuration. In those cases, the programs decide that one or the other takes
precedence. For another exercise on your own, try controlling case sensitivity
through either a command line argument or an environment variable. Decide
whether the command line argument or the environment variable should take
precedence if the program is run with one set to case sensitive and one set to
ignore case.

The `std::env` module contains many more useful features for dealing with
environment variables: check out its documentation to see what is available.
