# Using a Crate to Get More Functionality

Remember that a crate is a collection of Rust source code files. The project
we’ve been building is a _binary crate_, which is an executable. The `rand`
crate is a _library crate_, which contains code that is intended to be used in
other programs and can’t be executed on its own.

Cargo’s coordination of external crates is where Cargo really shines. Before we
can write code that uses `rand`, we need to modify the `Cargo.toml` file to
include the `rand` crate as a dependency. Open that file now and add the
following line to the bottom, beneath the `[dependencies]` section header that
Cargo created for you. Be sure to specify `rand` exactly as we have here, with
this version number, or the code examples in this tutorial may not work:

Filename: `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

In the `Cargo.toml` file, everything that follows a header is part of that
section that continues until another section starts. In `[dependencies]` you
tell Cargo which external crates your project depends on and which versions of
those crates you require. In this case, we specify the `rand` crate with the
semantic version specifier `0.8.5`. Cargo understands Semantic Versioning
(sometimes called _SemVer_), which is a standard for writing version numbers.
The specifier `0.8.5` is actually shorthand for `^0.8.5`, which means any
version that is at least 0.8.5 but below 0.9.0.

Cargo considers these versions to have public APIs compatible with version
0.8.5, and this specification ensures you’ll get the latest patch release that
will still compile with the code in this chapter. Any version 0.9.0 or greater
is not guaranteed to have the same API as what the following examples use.

Now, without changing any of the code, let’s build the project, as shown in
Listing 2-2.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Listing 2-2: The output from running `cargo build` after adding the `rand`
crate as a dependency

You may see different version numbers (but they will all be compatible with the
code, thanks to SemVer!) and different lines (depending on the operating
system), and the lines may be in a different order.

When we include an external dependency, Cargo fetches the latest versions of
everything that dependency needs from the _registry_, which is a copy of data
from Crates.io at *https://crates.io*. Crates.io is where people in the Rust
ecosystem post their open source Rust projects for others to use.

After updating the registry, Cargo checks the `[dependencies]` section and
downloads any crates listed that aren’t already downloaded. In this case,
although we only listed `rand` as a dependency, Cargo also grabbed other crates
that `rand` depends on to work. After downloading the crates, Rust compiles
them and then compiles the project with the dependencies available.

If you immediately run `cargo build` again without making any changes, you
won’t get any output aside from the `Finished` line. Cargo knows it has already
downloaded and compiled the dependencies, and you haven’t changed anything
about them in your `Cargo.toml` file. Cargo also knows that you haven’t changed
anything about your code, so it doesn’t recompile that either. With nothing to
do, it simply exits.

If you open the `src/main.rs` file, make a trivial change, and then save it and
build again, you’ll only see two lines of output:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

These lines show that Cargo only updates the build with your tiny change to the
`src/main.rs` file. Your dependencies haven’t changed, so Cargo knows it can
reuse what it has already downloaded and compiled for those.

#
