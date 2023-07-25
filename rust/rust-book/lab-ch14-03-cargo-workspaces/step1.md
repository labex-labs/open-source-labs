# Cargo Workspaces

In Chapter 12, we built a package that included a binary crate and a library
crate. As your project develops, you might find that the library crate
continues to get bigger and you want to split your package further into
multiple library crates. Cargo offers a feature called _workspaces_ that can
help manage multiple related packages that are developed in tandem.
