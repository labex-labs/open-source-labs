# Implementing the Trait

Now we’ll add some types that implement the `Draw` trait. We’ll provide the
`Button` type. Again, actually implementing a GUI library is beyond the scope
of this book, so the `draw` method won’t have any useful implementation in its
body. To imagine what the implementation might look like, a `Button` struct
might have fields for `width`, `height`, and `label`, as shown in Listing 17-7.

Filename: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // code to actually draw a button
    }
}
```

Listing 17-7: A `Button` struct that implements the `Draw` trait

The `width`, `height`, and `label` fields on `Button` will differ from the
fields on other components; for example, a `TextField` type might have those
same fields plus a `placeholder` field. Each of the types we want to draw on
the screen will implement the `Draw` trait but will use different code in the
`draw` method to define how to draw that particular type, as `Button` has here
(without the actual GUI code, as mentioned). The `Button` type, for instance,
might have an additional `impl` block containing methods related to what
happens when a user clicks the button. These kinds of methods won’t apply to
types like `TextField`.

If someone using our library decides to implement a `SelectBox` struct that has
`width`, `height`, and `options` fields, they would implement the `Draw` trait
on the `SelectBox` type as well, as shown in Listing 17-8.

Filename: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // code to actually draw a select box
    }
}
```

Listing 17-8: Another crate using `gui` and implementing the `Draw` trait on a
`SelectBox` struct

Our library’s user can now write their `main` function to create a `Screen`
instance. To the `Screen` instance, they can add a `SelectBox` and a `Button`
by putting each in a `Box<T>` to become a trait object. They can then call the
`run` method on the `Screen` instance, which will call `draw` on each of the
components. Listing 17-9 shows this implementation.

Filename: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Listing 17-9: Using trait objects to store values of different types that
implement the same trait

When we wrote the library, we didn’t know that someone might add the
`SelectBox` type, but our `Screen` implementation was able to operate on the
new type and draw it because `SelectBox` implements the `Draw` trait, which
means it implements the `draw` method.

This concept—of being concerned only with the messages a value responds to
rather than the value’s concrete type—is similar to the concept of _duck
typing_ in dynamically typed languages: if it walks like a duck and quacks like
a duck, then it must be a duck! In the implementation of `run` on `Screen` in
Listing 17-5, `run` doesn’t need to know what the concrete type of each
component is. It doesn’t check whether a component is an instance of a `Button`
or a `SelectBox`, it just calls the `draw` method on the component. By
specifying `Box<dyn Draw>` as the type of the values in the `components`
vector, we’ve defined `Screen` to need values that we can call the `draw`
method on.

The advantage of using trait objects and Rust’s type system to write code
similar to code using duck typing is that we never have to check whether a
value implements a particular method at runtime or worry about getting errors
if a value doesn’t implement a method but we call it anyway. Rust won’t compile
our code if the values don’t implement the traits that the trait objects need.

For example, Listing 17-10 shows what happens if we try to create a `Screen`
with a `String` as a component.

Filename: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Listing 17-10: Attempting to use a type that doesn’t implement the trait
object’s trait

We’ll get this error because `String` doesn’t implement the `Draw` trait:

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

This error lets us know that either we’re passing something to `Screen` that we
didn’t mean to pass and so should pass a different type, or we should implement
`Draw` on `String` so that `Screen` is able to call `draw` on it.
