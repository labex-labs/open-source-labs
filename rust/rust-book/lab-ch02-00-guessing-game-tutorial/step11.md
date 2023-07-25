# Ensuring Reproducible Builds with the Cargo.lock File

Cargo has a mechanism that ensures you can rebuild the same artifact every time
you or anyone else builds your code: Cargo will use only the versions of the
dependencies you specified until you indicate otherwise. For example, say that
next week version 0.8.6 of the `rand` crate comes out, and that version
contains an important bug fix, but it also contains a regression that will
break your code. To handle this, Rust creates the _Cargo.lock_ file the first
time you run `cargo build`, so we now have this in the _guessing_game_
directory.

When you build a project for the first time, Cargo figures out all the versions
of the dependencies that fit the criteria and then writes them to the
_Cargo.lock_ file. When you build your project in the future, Cargo will see
that the _Cargo.lock_ file exists and will use the versions specified there
rather than doing all the work of figuring out versions again. This lets you
have a reproducible build automatically. In other words, your project will
remain at 0.8.5 until you explicitly upgrade, thanks to the _Cargo.lock_ file.
Because the _Cargo.lock_ file is important for reproducible builds, it’s often
checked into source control with the rest of the code in your project.

#
