# Packages and Crates

The first parts of the module system we’ll cover are packages and crates.

A _crate_ is the smallest amount of code that the Rust compiler considers at a
time. Even if you run `rustc` rather than `cargo` and pass a single source code
file (as we did all the way back in “Writing and Running a Rust Program” on
page XX), the compiler considers that file to be a crate. Crates can contain
modules, and the modules may be defined in other files that get compiled with
the crate, as we’ll see in the coming sections.

A crate can come in one of two forms: a binary crate or a library crate.
_Binary crates_ are programs you can compile to an executable that you can run,
such as a command line program or a server. Each must have a function called
`main` that defines what happens when the executable runs. All the crates we’ve
created so far have been binary crates.

_Library crates_ don’t have a `main` function, and they don’t compile to an
executable. Instead, they define functionality intended to be shared with
multiple projects. For example, the `rand` crate we used in Chapter 2 provides
functionality that generates random numbers. Most of the time when Rustaceans
say “crate,” they mean library crate, and they use “crate” interchangeably with
the general programming concept of a “library.”

The _crate root_ is a source file that the Rust compiler starts from and makes
up the root module of your crate (we’ll explain modules in depth in “Defining
Modules to Control Scope and Privacy” on page XX).

A _package_ is a bundle of one or more crates that provides a set of
functionality. A package contains a `Cargo.toml` file that describes how to
build those crates. Cargo is actually a package that contains the binary crate
for the command line tool you’ve been using to build your code. The Cargo
package also contains a library crate that the binary crate depends on. Other
projects can depend on the Cargo library crate to use the same logic the Cargo
command line tool uses.

A crate can come in one of two forms: a binary crate or a library crate. A
package can contain as many binary crates as you like, but at most only one
library crate. A package must contain at least one crate, whether that’s a
library or binary crate.

Let’s walk through what happens when we create a package. First we enter the
command `cargo new my-project`:

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

After we run `cargo new my-project`, we use `ls` to see what Cargo creates. In
the project directory, there’s a `Cargo.toml` file, giving us a package.
There’s also a `src` directory that contains `main.rs`. Open `Cargo.toml` in
your text editor, and note there’s no mention of `src/main.rs`. Cargo follows a
convention that `src/main.rs` is the crate root of a binary crate with the same
name as the package. Likewise, Cargo knows that if the package directory
contains `src/lib.rs`, the package contains a library crate with the same name
as the package, and `src/lib.rs` is its crate root. Cargo passes the crate root
files to `rustc` to build the library or binary.

Here, we have a package that only contains `src/main.rs`, meaning it only
contains a binary crate named `my-project`. If a package contains `src/main.rs`
and `src/lib.rs`, it has two crates: a binary and a library, both with the same
name as the package. A package can have multiple binary crates by placing files
in the `src/bin` directory: each file will be a separate binary crate.

> **Modules Cheat Sheet**
>
> Before we get to the details of modules and paths, here we provide a quick
> reference on how modules, paths, the `use` keyword, and the `pub` keyword work
> in the compiler, and how most developers organize their code. We’ll be going
> through examples of each of these rules throughout this chapter, but this is a
> great place to refer to as a reminder of how modules work.
>
> - **Start from the crate root**: When compiling a crate, the compiler first
>   looks in the crate root file (usually `src/lib.rs` for a library crate or
>   `src/main.rs` for a binary crate) for code to compile.
> - **Declaring modules**: In the crate root file, you can declare new modules;
>   say you declare a “garden” module with `mod garden;`. The compiler will look
>   for the module’s code in these places:
>
> - Inline, within curly brackets that replace the semicolon following `mod
garden`
> - In the file `src/garden.rs`
> - In the file `src/garden/mod.rs`
> - **Declaring submodules**: In any file other than the crate root, you can
>   declare submodules. For example, you might declare `mod vegetables;` in
>   `src/garden.rs`. The compiler will look for the submodule’s code within the
>   directory named for the parent module in these places:
>
> - Inline, directly following `mod vegetables`, within curly brackets instead
>   of the semicolon
> - In the file `src/garden/vegetables.rs`
> - In the file `src/garden/vegetables/mod.rs`
> - **Paths to code in modules**: Once a module is part of your crate, you can
>   refer to code in that module from anywhere else in that same crate, as long as
>   the privacy rules allow, using the path to the code. For example, an
>   `Asparagus` type in the garden vegetables module would be found at
>   `crate::garden::vegetables::Asparagus`.
> - **Private vs. public**: Code within a module is private from its parent
>   modules by default. To make a module public, declare it with `pub mod` instead
>   of `mod`. To make items within a public module public as well, use `pub` before
>   their declarations.
> - **The use keyword**: Within a scope, the `use` keyword creates shortcuts to
>   items to reduce repetition of long paths. In any scope that can refer to
>   `crate::garden::vegetables::Asparagus`, you can create a shortcut with `use
crate::garden::vegetables::Asparagus;` and from then on you only need to write
>   `Asparagus` to make use of that type in the scope.
>
> Here, we create a binary crate named `backyard` that illustrates these rules.
> The crate’s directory, also named `backyard`, contains these files and
> directories:
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> The crate root file in this case is `src/main.rs`, and it contains:
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> The `pub mod garden;` line tells the compiler to include the code it finds in
> `src/garden.rs`, which is:
>
> ```rust
> pub mod vegetables;
> ```
>
> Here, `pub mod vegetables;` means the code in `src/garden/vegetables.rs` is
> included too. That code is:
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> Now let’s get into the details of these rules and demonstrate them in action!
