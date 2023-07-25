# Dereferencing a Raw Pointer

In “Dangling References” on page XX, we mentioned that the compiler ensures
references are always valid. Unsafe Rust has two new types called _raw
pointers_ that are similar to references. As with references, raw pointers can
be immutable or mutable and are written as `*const T` and `*mut T`,
respectively. The asterisk isn’t the dereference operator; it’s part of the
type name. In the context of raw pointers, _immutable_ means that the pointer
can’t be directly assigned to after being dereferenced.

Different from references and smart pointers, raw pointers:

- Are allowed to ignore the borrowing rules by having both immutable and
  mutable pointers or multiple mutable pointers to the same location
- Aren’t guaranteed to point to valid memory
- Are allowed to be null
- Don’t implement any automatic cleanup

By opting out of having Rust enforce these guarantees, you can give up
guaranteed safety in exchange for greater performance or the ability to
interface with another language or hardware where Rust’s guarantees don’t apply.

Listing 19-1 shows how to create an immutable and a mutable raw pointer from
references.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;
```

Listing 19-1: Creating raw pointers from references

Notice that we don’t include the `unsafe` keyword in this code. We can create
raw pointers in safe code; we just can’t dereference raw pointers outside an
unsafe block, as you’ll see in a bit.

We’ve created raw pointers by using `as` to cast an immutable and a mutable
reference into their corresponding raw pointer types. Because we created them
directly from references guaranteed to be valid, we know these particular raw
pointers are valid, but we can’t make that assumption about just any raw
pointer.

To demonstrate this, next we’ll create a raw pointer whose validity we can’t be
so certain of. Listing 19-2 shows how to create a raw pointer to an arbitrary
location in memory. Trying to use arbitrary memory is undefined: there might be
data at that address or there might not, the compiler might optimize the code
so there is no memory access, or the program might terminate with a
segmentation fault. Usually, there is no good reason to write code like this,
but it is possible.

```rust
let address = 0x012345usize;
let r = address as *const i32;
```

Listing 19-2: Creating a raw pointer to an arbitrary memory address

Recall that we can create raw pointers in safe code, but we can’t _dereference_
raw pointers and read the data being pointed to. In Listing 19-3, we use the
dereference operator `*` on a raw pointer that requires an `unsafe` block.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

Listing 19-3: Dereferencing raw pointers within an `unsafe` block

Creating a pointer does no harm; it’s only when we try to access the value that
it points at that we might end up dealing with an invalid value.

Note also that in Listings 19-1 and 19-3, we created `*const i32` and `*mut
i32` raw pointers that both pointed to the same memory location, where `num` is
stored. If we instead tried to create an immutable and a mutable reference to
`num`, the code would not have compiled because Rust’s ownership rules don’t
allow a mutable reference at the same time as any immutable references. With
raw pointers, we can create a mutable pointer and an immutable pointer to the
same location and change data through the mutable pointer, potentially creating
a data race. Be careful!

With all of these dangers, why would you ever use raw pointers? One major use
case is when interfacing with C code, as you’ll see in “Calling an Unsafe
Function or Method” on page XX. Another case is when building up safe
abstractions that the borrow checker doesn’t understand. We’ll introduce unsafe
functions and then look at an example of a safe abstraction that uses unsafe
code.
