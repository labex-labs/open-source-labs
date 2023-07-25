# Adding Useful Functionality with Derived Traits

It’d be useful to be able to print an instance of `Rectangle` while we’re
debugging our program and see the values for all its fields. Listing 5-11 tries
using the `println!` macro as we have used in previous chapters. This won’t
work, however.

Filename: `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1);
}
```

Listing 5-11: Attempting to print a `Rectangle` instance

When we compile this code, we get an error with this core message:

```bash
error[E0277]: `Rectangle` doesn't implement `std::fmt::Display`
```

The `println!` macro can do many kinds of formatting, and by default, the curly
brackets tell `println!` to use formatting known as `Display`: output intended
for direct end user consumption. The primitive types we’ve seen so far
implement `Display` by default because there’s only one way you’d want to show
a `1` or any other primitive type to a user. But with structs, the way
`println!` should format the output is less clear because there are more
display possibilities: Do you want commas or not? Do you want to print the
curly brackets? Should all the fields be shown? Due to this ambiguity, Rust
doesn’t try to guess what we want, and structs don’t have a provided
implementation of `Display` to use with `println!` and the `{}` placeholder.

If we continue reading the errors, we’ll find this helpful note:

```
= help: the trait `std::fmt::Display` is not implemented for `Rectangle`
= note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
```

Let’s try it! The `println!` macro call will now look like `println!("rect1 is
{:?}", rect1);`. Putting the specifier `:?` inside the curly brackets tells
`println!` we want to use an output format called `Debug`. The `Debug` trait
enables us to print our struct in a way that is useful for developers so we can
see its value while we’re debugging our code.

Compile the code with this change. Drat! We still get an error:

```bash
error[E0277]: `Rectangle` doesn't implement `Debug`
```

But again, the compiler gives us a helpful note:

```rust
= help: the trait `Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` or manually implement `Debug`
```

Rust _does_ include functionality to print out debugging information, but we
have to explicitly opt in to make that functionality available for our struct.
To do that, we add the outer attribute `#[derive(Debug)]` just before the
struct definition, as shown in Listing 5-12.

Filename: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

Listing 5-12: Adding the attribute to derive the `Debug` trait and printing the
`Rectangle` instance using debug formatting

Now when we run the program, we won’t get any errors, and we’ll see the
following output:

```rust
rect1 is Rectangle { width: 30, height: 50 }
```

Nice! It’s not the prettiest output, but it shows the values of all the fields
for this instance, which would definitely help during debugging. When we have
larger structs, it’s useful to have output that’s a bit easier to read; in
those cases, we can use `{:#?}` instead of `{:?}` in the `println!` string. In
this example, using the `{:#?}` style will output the following:

```
rect1 is Rectangle {
    width: 30,
    height: 50,
}
```

Another way to print out a value using the `Debug` format is to use the `dbg!`
macro, which takes ownership of an expression (as opposed to `println!`, which
takes a reference), prints the file and line number of where that `dbg!` macro
call occurs in your code along with the resultant value of that expression, and
returns ownership of the value.

> Note: Calling the `dbg!` macro prints to the standard error console stream
> (`stderr`), as opposed to `println!`, which prints to the standard output
> console stream (`stdout`). We’ll talk more about `stderr` and `stdout` in
> “Writing Error Messages to Standard Error Instead of Standard Output” on page
> XX.

Here’s an example where we’re interested in the value that gets assigned to the
`width` field, as well as the value of the whole struct in `rect1`:

Filename: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

We can put `dbg!` around the expression `30 * scale` [1] and, because `dbg!`
returns ownership of the expression’s value, the `width` field will get the
same value as if we didn’t have the `dbg!` call there. We don’t want `dbg!` to
take ownership of `rect1`, so we use a reference to `rect1` in the next call
[2]. Here’s what the output of this example looks like:

```
[src/main.rs:10] 30 * scale = 60
[src/main.rs:14] &rect1 = Rectangle {
    width: 60,
    height: 50,
}
```

We can see the first bit of output came from [1] where we’re debugging the
expression `30 * scale`, and its resultant value is `60` (the `Debug`
formatting implemented for integers is to print only their value). The `dbg!`
call at [2] outputs the value of `&rect1`, which is the `Rectangle` struct.
This output uses the pretty `Debug` formatting of the `Rectangle` type. The
`dbg!` macro can be really helpful when you’re trying to figure out what your
code is doing!

In addition to the `Debug` trait, Rust has provided a number of traits for us
to use with the `derive` attribute that can add useful behavior to our custom
types. Those traits and their behaviors are listed in Appendix C. We’ll cover
how to implement these traits with custom behavior as well as how to create
your own traits in Chapter 10. There are also many attributes other than
`derive`; for more information, see the “Attributes” section of the Rust
Reference at *https://doc.rust-lang.org/reference/attributes.html*.

Our `area` function is very specific: it only computes the area of rectangles.
It would be helpful to tie this behavior more closely to our `Rectangle` struct
because it won’t work with any other type. Let’s look at how we can continue to
refactor this code by turning the `area` function into an `area` _method_
defined on our `Rectangle` type.
