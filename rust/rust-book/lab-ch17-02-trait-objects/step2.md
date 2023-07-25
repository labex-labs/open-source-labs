# Defining a Trait for Common Behavior

To implement the behavior we want `gui` to have, we’ll define a trait named
`Draw` that will have one method named `draw`. Then we can define a vector that
takes a _trait object_. A trait object points to both an instance of a type
implementing our specified trait and a table used to look up trait methods on
that type at runtime. We create a trait object by specifying some sort of
pointer, such as a `&` reference or a `Box<T>` smart pointer, then the `dyn`
keyword, and then specifying the relevant trait. (We’ll talk about the reason
trait objects must use a pointer in “Dynamically Sized Types and the Sized
Trait” on page XX.) We can use trait objects in place of a generic or concrete
type. Wherever we use a trait object, Rust’s type system will ensure at compile
time that any value used in that context will implement the trait object’s
trait. Consequently, we don’t need to know all the possible types at compile
time.

We’ve mentioned that, in Rust, we refrain from calling structs and enums
“objects” to distinguish them from other languages’ objects. In a struct or
enum, the data in the struct fields and the behavior in `impl` blocks are
separated, whereas in other languages, the data and behavior combined into one
concept is often labeled an object. However, trait objects _are_ more like
objects in other languages in the sense that they combine data and behavior.
But trait objects differ from traditional objects in that we can’t add data to
a trait object. Trait objects aren’t as generally useful as objects in other
languages: their specific purpose is to allow abstraction across common
behavior.

Listing 17-3 shows how to define a trait named `Draw` with one method named
`draw`.

Filename: `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Listing 17-3: Definition of the `Draw` trait

This syntax should look familiar from our discussions on how to define traits
in Chapter 10. Next comes some new syntax: Listing 17-4 defines a struct named
`Screen` that holds a vector named `components`. This vector is of type
`Box<dyn Draw>`, which is a trait object; it’s a stand-in for any type inside a
`Box` that implements the `Draw` trait.

Filename: `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Listing 17-4: Definition of the `Screen` struct with a `components` field
holding a vector of trait objects that implement the `Draw` trait

On the `Screen` struct, we’ll define a method named `run` that will call the
`draw` method on each of its `components`, as shown in Listing 17-5.

Filename: `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-5: A `run` method on `Screen` that calls the `draw` method on each
component

This works differently from defining a struct that uses a generic type
parameter with trait bounds. A generic type parameter can only be substituted
with one concrete type at a time, whereas trait objects allow for multiple
concrete types to fill in for the trait object at runtime. For example, we
could have defined the `Screen` struct using a generic type and a trait bound,
as in Listing 17-6.

Filename: `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-6: An alternate implementation of the `Screen` struct and its `run`
method using generics and trait bounds

This restricts us to a `Screen` instance that has a list of components all of
type `Button` or all of type `TextField`. If you’ll only ever have homogeneous
collections, using generics and trait bounds is preferable because the
definitions will be monomorphized at compile time to use the concrete types.

On the other hand, with the method using trait objects, one `Screen` instance
can hold a `Vec<T>` that contains a `Box<Button>` as well as a
`Box<TextField>`. Let’s look at how this works, and then we’ll talk about the
runtime performance implications.
