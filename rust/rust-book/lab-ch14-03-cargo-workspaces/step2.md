# Creating a Workspace

A _workspace_ is a set of packages that share the same _Cargo.lock_ and output
directory. Let’s make a project using a workspace—we’ll use trivial code so we
can concentrate on the structure of the workspace. There are multiple ways to
structure a workspace, so we’ll just show one common way. We’ll have a
workspace containing a binary and two libraries. The binary, which will provide
the main functionality, will depend on the two libraries. One library will
provide an `add_one` function and the other library an `add_two` function.
These three crates will be part of the same workspace. We’ll start by creating
a new directory for the workspace:

```bash
mkdir add
cd add
```

Next, in the `add` directory, we create the `Cargo.toml` file that will
configure the entire workspace. This file won’t have a `[package]` section.
Instead, it will start with a `[workspace]` section that will allow us to add
members to the workspace by specifying the path to the package with our binary
crate; in this case, that path is _adder_:

Filename: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Next, we’ll create the `adder` binary crate by running `cargo new` within the
`add` directory:

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

At this point, we can build the workspace by running `cargo build`. The files
in your `add` directory should look like this:

```
├── Cargo.lock
├── Cargo.toml
├── adder
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── target
```

The workspace has one `target` directory at the top level that the compiled
artifacts will be placed into; the `adder` package doesn’t have its own
`target` directory. Even if we were to run `cargo build` from inside the
`adder` directory, the compiled artifacts would still end up in _add/target_
rather than `add/adder/target`. Cargo structures the `target` directory in a
workspace like this because the crates in a workspace are meant to depend on
each other. If each crate had its own `target` directory, each crate would have
to recompile each of the other crates in the workspace to place the artifacts
in its own `target` directory. By sharing one `target` directory, the crates
can avoid unnecessary rebuilding.
