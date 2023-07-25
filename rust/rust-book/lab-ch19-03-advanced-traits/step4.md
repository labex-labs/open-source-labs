# Disambiguating Between Methods with the Same Name

Nothing in Rust prevents a trait from having a method with the same name as
another trait’s method, nor does Rust prevent you from implementing both traits
on one type. It’s also possible to implement a method directly on the type with
the same name as methods from traits.

When calling methods with the same name, you’ll need to tell Rust which one you
want to use. Consider the code in Listing 19-16 where we’ve defined two traits,
`Pilot` and `Wizard`, that both have a method called `fly`. We then implement
both traits on a type `Human` that already has a method named `fly` implemented
on it. Each `fly` method does something different.

Filename: `src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

Listing 19-16: Two traits are defined to have a `fly` method and are
implemented on the `Human` type, and a `fly` method is implemented on `Human`
directly.

When we call `fly` on an instance of `Human`, the compiler defaults to calling
the method that is directly implemented on the type, as shown in Listing 19-17.

Filename: `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Listing 19-17: Calling `fly` on an instance of `Human`

Running this code will print `*waving arms furiously*`, showing that Rust
called the `fly` method implemented on `Human` directly.

To call the `fly` methods from either the `Pilot` trait or the `Wizard` trait,
we need to use more explicit syntax to specify which `fly` method we mean.
Listing 19-18 demonstrates this syntax.

Filename: `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Listing 19-18: Specifying which trait’s `fly` method we want to call

Specifying the trait name before the method name clarifies to Rust which
implementation of `fly` we want to call. We could also write
`Human::fly(&person)`, which is equivalent to the `person.fly()` that we used
in Listing 19-18, but this is a bit longer to write if we don’t need to
disambiguate.

Running this code prints the following:

```
This is your captain speaking.
Up!
*waving arms furiously*
```

Because the `fly` method takes a `self` parameter, if we had two _types_ that
both implement one _trait_, Rust could figure out which implementation of a
trait to use based on the type of `self`.

However, associated functions that are not methods don’t have a `self`
parameter. When there are multiple types or traits that define non-method
functions with the same function name, Rust doesn’t always know which type you
mean unless you use fully qualified syntax. For example, in Listing 19-19 we
create a trait for an animal shelter that wants to name all baby dogs Spot. We
make an `Animal` trait with an associated non-method function `baby_name`. The
`Animal` trait is implemented for the struct `Dog`, on which we also provide an
associated non-method function `baby_name` directly.

Filename: `src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

Listing 19-19: A trait with an associated function and a type with an
associated function of the same name that also implements the trait

We implement the code for naming all puppies Spot in the `baby_name` associated
function that is defined on `Dog`. The `Dog` type also implements the trait
`Animal`, which describes characteristics that all animals have. Baby dogs are
called puppies, and that is expressed in the implementation of the `Animal`
trait on `Dog` in the `baby_name` function associated with the `Animal` trait.

In `main`, we call the `Dog::baby_name` function, which calls the associated
function defined on `Dog` directly. This code prints the following:

```rust
A baby dog is called a Spot
```

This output isn’t what we wanted. We want to call the `baby_name` function that
is part of the `Animal` trait that we implemented on `Dog` so the code prints
`A baby dog is called a puppy`. The technique of specifying the trait name that
we used in Listing 19-18 doesn’t help here; if we change `main` to the code in
Listing 19-20, we’ll get a compilation error.

Filename: `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Listing 19-20: Attempting to call the `baby_name` function from the `Animal`
trait, but Rust doesn’t know which implementation to use

Because `Animal::baby_name` doesn’t have a `self` parameter, and there could be
other types that implement the `Animal` trait, Rust can’t figure out which
implementation of `Animal::baby_name` we want. We’ll get this compiler error:

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

To disambiguate and tell Rust that we want to use the implementation of
`Animal` for `Dog` as opposed to the implementation of `Animal` for some other
type, we need to use fully qualified syntax. Listing 19-21 demonstrates how to
use fully qualified syntax.

Filename: `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Listing 19-21: Using fully qualified syntax to specify that we want to call the
`baby_name` function from the `Animal` trait as implemented on `Dog`

We’re providing Rust with a type annotation within the angle brackets, which
indicates we want to call the `baby_name` method from the `Animal` trait as
implemented on `Dog` by saying that we want to treat the `Dog` type as an
`Animal` for this function call. This code will now print what we want:

```rust
A baby dog is called a puppy
```

In general, fully qualified syntax is defined as follows:

```rust
<Type as Trait>::function(receiver_if_method, next_arg, ...);
```

For associated functions that aren’t methods, there would not be a `receiver`:
there would only be the list of other arguments. You could use fully qualified
syntax everywhere that you call functions or methods. However, you’re allowed
to omit any part of this syntax that Rust can figure out from other information
in the program. You only need to use this more verbose syntax in cases where
there are multiple implementations that use the same name and Rust needs help
to identify which implementation you want to call.
