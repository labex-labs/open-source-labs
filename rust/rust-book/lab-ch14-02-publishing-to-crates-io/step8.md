# Adding Metadata to a New Crate

Let’s say you have a crate you want to publish. Before publishing, you’ll need
to add some metadata in the `[package]` section of the crate’s `Cargo.toml`
file.

Your crate will need a unique name. While you’re working on a crate locally,
you can name a crate whatever you’d like. However, crate names on
*https://crates.io* are allocated on a first-come, first-served basis. Once a
crate name is taken, no one else can publish a crate with that name. Before
attempting to publish a crate, search for the name you want to use. If the name
has been used, you will need to find another name and edit the `name` field in
the `Cargo.toml` file under the `[package]` section to use the new name for
publishing, like so:

Filename: `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

Even if you’ve chosen a unique name, when you run `cargo publish` to publish
the crate at this point, you’ll get a warning and then an error:

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

This results in an error because you’re missing some crucial information: a
description and license are required so people will know what your crate does
and under what terms they can use it. In `Cargo.toml`, add a description that’s
just a sentence or two, because it will appear with your crate in search
results. For the `license` field, you need to give a _license identifier
value_. The Linux Foundation’s Software Package Data Exchange (SPDX) at
*http://spdx.org/licenses* lists the identifiers you can use for this value.
For example, to specify that you’ve licensed your crate using the MIT License,
add the `MIT` identifier:

Filename: `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

If you want to use a license that doesn’t appear in the SPDX, you need to place
the text of that license in a file, include the file in your project, and then
use `license-file` to specify the name of that file instead of using the
`license` key.

Guidance on which license is appropriate for your project is beyond the scope
of this book. Many people in the Rust community license their projects in the
same way as Rust by using a dual license of `MIT OR Apache-2.0`. This practice
demonstrates that you can also specify multiple license identifiers separated
by `OR` to have multiple licenses for your project.

With a unique name, the version, your description, and a license added, the
`Cargo.toml` file for a project that is ready to publish might look like this:

Filename: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

Cargo’s documentation at *https://doc.rust-lang.org/cargo* describes other
metadata you can specify to ensure that others can discover and use your crate
more easily.
