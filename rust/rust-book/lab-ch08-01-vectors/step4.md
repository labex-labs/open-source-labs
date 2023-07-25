# Reading Elements of Vectors

There are two ways to reference a value stored in a vector: via indexing or by
using the `get` method. In the following examples, we’ve annotated the types of
the values that are returned from these functions for extra clarity.

Listing 8-4 shows both methods of accessing a value in a vector, with indexing
syntax and the `get` method.

```rust
let v = vec![1, 2, 3, 4, 5];

1 let third: &i32 = &v[2];
println!("The third element is {third}");

2 let third: Option<&i32> = v.get(2);
match third  {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

Listing 8-4: Using indexing syntax and using the `get` method to access an item
in a vector

Note a few details here. We use the index value of `2` to get the third element
[1] because vectors are indexed by number, starting at zero. Using `&` and `[]`
gives us a reference to the element at the index value. When we use the `get`
method with the index passed as an argument [2], we get an `Option<&T>` that we
can use with `match`.

Rust provides these two ways to reference an element so you can choose how the
program behaves when you try to use an index value outside the range of
existing elements. As an example, let’s see what happens when we have a vector
of five elements and then we try to access an element at index 100 with each
technique, as shown in Listing 8-5.

```rust
let v = vec![1, 2, 3, 4, 5];

let does_not_exist = &v[100];
let does_not_exist = v.get(100);
```

Listing 8-5: Attempting to access the element at index 100 in a vector
containing five elements

When we run this code, the first `[]` method will cause the program to panic
because it references a nonexistent element. This method is best used when you
want your program to crash if there’s an attempt to access an element past the
end of the vector.

When the `get` method is passed an index that is outside the vector, it returns
`None` without panicking. You would use this method if accessing an element
beyond the range of the vector may happen occasionally under normal
circumstances. Your code will then have logic to handle having either
`Some(&element)` or `None`, as discussed in Chapter 6. For example, the index
could be coming from a person entering a number. If they accidentally enter a
number that’s too large and the program gets a `None` value, you could tell the
user how many items are in the current vector and give them another chance to
enter a valid value. That would be more user-friendly than crashing the program
due to a typo!

When the program has a valid reference, the borrow checker enforces the
ownership and borrowing rules (covered in Chapter 4) to ensure this reference
and any other references to the contents of the vector remain valid. Recall the
rule that states you can’t have mutable and immutable references in the same
scope. That rule applies in Listing 8-6, where we hold an immutable reference
to the first element in a vector and try to add an element to the end. This
program won’t work if we also try to refer to that element later in the
function.

```rust
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);

println!("The first element is: {first}");
```

Listing 8-6: Attempting to add an element to a vector while holding a reference
to an item

Compiling this code will result in this error:

```bash
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:5
  |
4 |     let first = &v[0];
  |                  - immutable borrow occurs here
5 |
6 |     v.push(6);
  |     ^^^^^^^^^ mutable borrow occurs here
7 |
8 |     println!("The first element is: {first}");
  |                                      ----- immutable borrow later used here
```

The code in Listing 8-6 might look like it should work: why should a reference
to the first element care about changes at the end of the vector? This error is
due to the way vectors work: because vectors put the values next to each other
in memory, adding a new element onto the end of the vector might require
allocating new memory and copying the old elements to the new space, if there
isn’t enough room to put all the elements next to each other where the vector
is currently stored. In that case, the reference to the first element would be
pointing to deallocated memory. The borrowing rules prevent programs from
ending up in that situation.

> Note: For more on the implementation details of the `Vec<T>` type, see “The
> Rustonomicon” at *https://doc.rust-lang.org/nomicon/vec/vec.html*.
