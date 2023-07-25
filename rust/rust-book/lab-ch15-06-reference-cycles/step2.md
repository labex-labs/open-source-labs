# Creating a Reference Cycle

Let’s look at how a reference cycle might happen and how to prevent it,
starting with the definition of the `List` enum and a `tail` method in Listing
15-25.

Filename: `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Listing 15-25: A cons list definition that holds a `RefCell<T>` so we can
modify what a `Cons` variant is referring to

We’re using another variation of the `List` definition from Listing 15-5. The
second element in the `Cons` variant is now `RefCell<Rc<List>>` [1], meaning
that instead of having the ability to modify the `i32` value as we did in
Listing 15-24, we want to modify the `List` value a `Cons` variant is pointing
to. We’re also adding a `tail` method [2] to make it convenient for us to
access the second item if we have a `Cons` variant.

In Listing 15-26, we’re adding a `main` function that uses the definitions in
Listing 15-25. This code creates a list in `a` and a list in `b` that points to
the list in `a`. Then it modifies the list in `a` to point to `b`, creating a
reference cycle. There are `println!` statements along the way to show what the
reference counts are at various points in this process.

Filename: `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Uncomment the next line to see that we have a cycle;
    // it will overflow the stack
    // println!("a next item = {:?}", a.tail());
}
```

Listing 15-26: Creating a reference cycle of two `List` values pointing to each
other

We create an `Rc<List>` instance holding a `List` value in the variable `a`
with an initial list of `5, Nil` [1]. We then create an `Rc<List>` instance
holding another `List` value in the variable `b` that contains the value `10`
and points to the list in `a` [2].

We modify `a` so it points to `b` instead of `Nil`, creating a cycle. We do
that by using the `tail` method to get a reference to the `RefCell<Rc<List>>`
in `a`, which we put in the variable `link` [3]. Then we use the `borrow_mut`
method on the `RefCell<Rc<List>>` to change the value inside from an `Rc<List>`
that holds a `Nil` value to the `Rc<List>` in `b` [4].

When we run this code, keeping the last `println!` commented out for the
moment, we’ll get this output:

```
a initial rc count = 1
a next item = Some(RefCell { value: Nil })
a rc count after b creation = 2
b initial rc count = 1
b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
b rc count after changing a = 2
a rc count after changing a = 2
```

The reference count of the `Rc<List>` instances in both `a` and `b` is 2 after
we change the list in `a` to point to `b`. At the end of `main`, Rust drops the
variable `b`, which decreases the reference count of the `b` `Rc<List>`
instance from 2 to 1. The memory that `Rc<List>` has on the heap won’t be
dropped at this point because its reference count is 1, not 0. Then Rust drops
`a`, which decreases the reference count of the `a` `Rc<List>` instance from 2
to 1 as well. This instance’s memory can’t be dropped either, because the other
`Rc<List>` instance still refers to it. The memory allocated to the list will
remain uncollected forever. To visualize this reference cycle, we’ve created a
diagram in Figure 15-4.

Figure 15-4: A reference cycle of lists `a` and `b` pointing to each other

If you uncomment the last `println!` and run the program, Rust will try to
print this cycle with `a` pointing to `b` pointing to `a` and so forth until it
overflows the stack.

Compared to a real-world program, the consequences of creating a reference
cycle in this example aren’t very dire: right after we create the reference
cycle, the program ends. However, if a more complex program allocated lots of
memory in a cycle and held onto it for a long time, the program would use more
memory than it needed and might overwhelm the system, causing it to run out of
available memory.

Creating reference cycles is not easily done, but it’s not impossible either.
If you have `RefCell<T>` values that contain `Rc<T>` values or similar nested
combinations of types with interior mutability and reference counting, you must
ensure that you don’t create cycles; you can’t rely on Rust to catch them.
Creating a reference cycle would be a logic bug in your program that you should
use automated tests, code reviews, and other software development practices to
minimize.

Another solution for avoiding reference cycles is reorganizing your data
structures so that some references express ownership and some references don’t.
As a result, you can have cycles made up of some ownership relationships and
some non-ownership relationships, and only the ownership relationships affect
whether or not a value can be dropped. In Listing 15-25, we always want `Cons`
variants to own their list, so reorganizing the data structure isn’t possible.
Let’s look at an example using graphs made up of parent nodes and child nodes
to see when non-ownership relationships are an appropriate way to prevent
reference cycles.
