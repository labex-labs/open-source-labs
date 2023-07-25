# Running Code on Cleanup with the Drop Trait

The second trait important to the smart pointer pattern is `Drop`, which lets
you customize what happens when a value is about to go out of scope. You can
provide an implementation for the `Drop` trait on any type, and that code can
be used to release resources like files or network connections.

We’re introducing `Drop` in the context of smart pointers because the
functionality of the `Drop` trait is almost always used when implementing a
smart pointer. For example, when a `Box<T>` is dropped it will deallocate the
space on the heap that the box points to.

In some languages, for some types, the programmer must call code to free memory
or resources every time they finish using an instance of those types. Examples
include file handles, sockets, and locks. If they forget, the system might
become overloaded and crash. In Rust, you can specify that a particular bit of
code be run whenever a value goes out of scope, and the compiler will insert
this code automatically. As a result, you don’t need to be careful about
placing cleanup code everywhere in a program that an instance of a particular
type is finished with—you still won’t leak resources!

You specify the code to run when a value goes out of scope by implementing the
`Drop` trait. The `Drop` trait requires you to implement one method named
`drop` that takes a mutable reference to `self`. To see when Rust calls `drop`,
let’s implement `drop` with `println!` statements for now.

Listing 15-14 shows a `CustomSmartPointer` struct whose only custom
functionality is that it will print `Dropping CustomSmartPointer!` when the
instance goes out of scope, to show when Rust runs the `drop` method.

Filename: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14: A `CustomSmartPointer` struct that implements the `Drop` trait
where we would put our cleanup code

The `Drop` trait is included in the prelude, so we don’t need to bring it into
scope. We implement the `Drop` trait on `CustomSmartPointer` [1] and provide an
implementation for the `drop` method that calls `println!` [2]. The body of the
`drop` method is where you would place any logic that you wanted to run when an
instance of your type goes out of scope. We’re printing some text here to
demonstrate visually when Rust will call `drop`.

In `main`, we create two instances of `CustomSmartPointer` at [3] and [4] and
then print `CustomSmartPointers created` [5]. At the end of `main` [6], our
instances of `CustomSmartPointer` will go out of scope, and Rust will call the
code we put in the `drop` method [2], printing our final message. Note that we
didn’t need to call the `drop` method explicitly.

When we run this program, we’ll see the following output:

```
CustomSmartPointers created.
Dropping CustomSmartPointer with data `other stuff`!
Dropping CustomSmartPointer with data `my stuff`!
```

Rust automatically called `drop` for us when our instances went out of scope,
calling the code we specified. Variables are dropped in the reverse order of
their creation, so `d` was dropped before `c`. This example’s purpose is to
give you a visual guide to how the `drop` method works; usually you would
specify the cleanup code that your type needs to run rather than a print
message.

Unfortunately, it’s not straightforward to disable the automatic `drop`
functionality. Disabling `drop` isn’t usually necessary; the whole point of the
`Drop` trait is that it’s taken care of automatically. Occasionally, however,
you might want to clean up a value early. One example is when using smart
pointers that manage locks: you might want to force the `drop` method that
releases the lock so that other code in the same scope can acquire the lock.
Rust doesn’t let you call the `Drop` trait’s `drop` method manually; instead,
you have to call the `std::mem::drop` function provided by the standard library
if you want to force a value to be dropped before the end of its scope.

If we try to call the `Drop` trait’s `drop` method manually by modifying the
`main` function from Listing 15-14, as shown in Listing 15-15, we’ll get a
compiler error.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15: Attempting to call the `drop` method from the `Drop` trait
manually to clean up early

When we try to compile this code, we’ll get this error:

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

This error message states that we’re not allowed to explicitly call `drop`. The
error message uses the term _destructor_, which is the general programming term
for a function that cleans up an instance. A _destructor_ is analogous to a
_constructor_, which creates an instance. The `drop` function in Rust is one
particular destructor.

Rust doesn’t let us call `drop` explicitly because Rust would still
automatically call `drop` on the value at the end of `main`. This would cause a
_double free_ error because Rust would be trying to clean up the same value
twice.

We can’t disable the automatic insertion of `drop` when a value goes out of
scope, and we can’t call the `drop` method explicitly. So, if we need to force
a value to be cleaned up early, we use the `std::mem::drop` function.

The `std::mem::drop` function is different from the `drop` method in the `Drop`
trait. We call it by passing as an argument the value we want to force-drop.
The function is in the prelude, so we can modify `main` in Listing 15-15 to
call the `drop` function, as shown in Listing 15-16.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16: Calling `std::mem::drop` to explicitly drop a value before it
goes out of scope

Running this code will print the following:

```
CustomSmartPointer created.
Dropping CustomSmartPointer with data `some data`!
CustomSmartPointer dropped before the end of main.
```

The text `Dropping CustomSmartPointer with data `some data`!` is printed
between the `CustomSmartPointer created.` and `CustomSmartPointer dropped
before the end of main.` text, showing that the `drop` method code is called to
drop `c` at that point.

You can use code specified in a `Drop` trait implementation in many ways to
make cleanup convenient and safe: for instance, you could use it to create your
own memory allocator! With the `Drop` trait and Rust’s ownership system, you
don’t have to remember to clean up because Rust does it automatically.

You also don’t have to worry about problems resulting from accidentally
cleaning up values still in use: the ownership system that makes sure
references are always valid also ensures that `drop` gets called only once when
the value is no longer being used.

Now that we’ve examined `Box<T>` and some of the characteristics of smart
pointers, let’s look at a few other smart pointers defined in the standard
library.