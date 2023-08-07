# Updating a Crate to Get a New Version

When you _do_ want to update a crate, Cargo provides the command `update`, which will ignore the _Cargo.lock_ file and figure out all the latest versions that fit your specifications in `Cargo.toml`. Cargo will then write those versions to the _Cargo.lock_ file. Otherwise, by default, Cargo will only look for versions greater than 0.8.5 and less than 0.9.0. If the `rand` crate has released the two new versions 0.8.6 and 0.9.0, you would see the following if you ran `cargo update`:

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

Cargo ignores the 0.9.0 release. At this point, you would also notice a change in your _Cargo.lock_ file noting that the version of the `rand` crate you are now using is 0.8.6. To use `rand` version 0.9.0 or any version in the 0.9.\_x\_ series, you'd have to update the `Cargo.toml` file to look like this instead:

```rust
[dependencies]
rand = "0.9.0"
```

The next time you run `cargo build`, Cargo will update the registry of crates available and reevaluate your `rand` requirements according to the new version you have specified.

There's a lot more to say about Cargo and its ecosystem, which we'll discuss in Chapter 14, but for now, that's all you need to know. Cargo makes it very easy to reuse libraries, so Rustaceans are able to write smaller projects that are assembled from a number of packages.
