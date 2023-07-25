# Playground

The [Rust Playground](https://play.rust-lang.org/) is a way to experiment with Rust code through a web interface.

## Using it with `mdbook`

In `mdbook`, you can make code examples playable and editable.

```rust
fn main() {
    println!("Hello World!");
}
```

This allows the reader to both run your code sample, but also modify and tweak it. The key here is the adding the word `editable` to your codefence block separated by a comma.

````markdown
```rust
//...place your code here
```
````

Additionally, you can add `ignore` if you want `mdbook` to skip your code when it builds and tests.

````markdown
```rust
//...place your code here
```
````

## Using it with docs

You may have noticed in some of the official Rust docs a button that says "Run", which opens the code sample up in a new tab in Rust Playground. This feature is enabled if you use the #[doc] attribute called `html_playground_url`.
