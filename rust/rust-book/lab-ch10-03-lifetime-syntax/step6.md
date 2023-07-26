# Lifetime Annotations in Function Signatures

To use lifetime annotations in function signatures, we need to declare the
generic _lifetime_ parameters inside angle brackets between the function name
and the parameter list, just as we did with generic _type_ parameters.

We want the signature to express the following constraint: the returned
reference will be valid as long as both the parameters are valid. This is the
relationship between lifetimes of the parameters and the return value. We’ll
name the lifetime `'a` and then add it to each reference, as shown in Listing
10-21.

Filename: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listing 10-21: The `longest` function definition specifying that all the
references in the signature must have the same lifetime `'a`

This code should compile and produce the result we want when we use it with the
`main` function in Listing 10-19.

The function signature now tells Rust that for some lifetime `'a`, the function
takes two parameters, both of which are string slices that live at least as
long as lifetime `'a`. The function signature also tells Rust that the string
slice returned from the function will live at least as long as lifetime `'a`.
In practice, it means that the lifetime of the reference returned by the
`longest` function is the same as the smaller of the lifetimes of the values
referred to by the function arguments. These relationships are what we want
Rust to use when analyzing this code.

Remember, when we specify the lifetime parameters in this function signature,
we’re not changing the lifetimes of any values passed in or returned. Rather,
we’re specifying that the borrow checker should reject any values that don’t
adhere to these constraints. Note that the `longest` function doesn’t need to
know exactly how long `x` and `y` will live, only that some scope can be
substituted for `'a` that will satisfy this signature.

When annotating lifetimes in functions, the annotations go in the function
signature, not in the function body. The lifetime annotations become part of
the contract of the function, much like the types in the signature. Having
function signatures contain the lifetime contract means the analysis the Rust
compiler does can be simpler. If there’s a problem with the way a function is
annotated or the way it is called, the compiler errors can point to the part of
our code and the constraints more precisely. If, instead, the Rust compiler
made more inferences about what we intended the relationships of the lifetimes
to be, the compiler might only be able to point to a use of our code many steps
away from the cause of the problem.

When we pass concrete references to `longest`, the concrete lifetime that is
substituted for `'a` is the part of the scope of `x` that overlaps with the
scope of `y`. In other words, the generic lifetime `'a` will get the concrete
lifetime that is equal to the smaller of the lifetimes of `x` and `y`. Because
we’ve annotated the returned reference with the same lifetime parameter `'a`,
the returned reference will also be valid for the length of the smaller of the
lifetimes of `x` and `y`.

Let’s look at how the lifetime annotations restrict the `longest` function by
passing in references that have different concrete lifetimes. Listing 10-22 is
a straightforward example.

Filename: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

Listing 10-22: Using the `longest` function with references to `String` values
that have different concrete lifetimes

In this example, `string1` is valid until the end of the outer scope, `string2`
is valid until the end of the inner scope, and `result` references something
that is valid until the end of the inner scope. Run this code and you’ll see
that the borrow checker approves; it will compile and print `The longest string
is long string is long`.

Next, let’s try an example that shows that the lifetime of the reference in
`result` must be the smaller lifetime of the two arguments. We’ll move the
declaration of the `result` variable outside the inner scope but leave the
assignment of the value to the `result` variable inside the scope with
`string2`. Then we’ll move the `println!` that uses `result` to outside the
inner scope, after the inner scope has ended. The code in Listing 10-23 will
not compile.

Filename: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

Listing 10-23: Attempting to use `result` after `string2` has gone out of scope

When we try to compile this code, we get this error:

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

The error shows that for `result` to be valid for the `println!` statement,
`string2` would need to be valid until the end of the outer scope. Rust knows
this because we annotated the lifetimes of the function parameters and return
values using the same lifetime parameter `'a`.

As humans, we can look at this code and see that `string1` is longer than
`string2`, and therefore, `result` will contain a reference to `string1`.
Because `string1` has not gone out of scope yet, a reference to `string1` will
still be valid for the `println!` statement. However, the compiler can’t see
that the reference is valid in this case. We’ve told Rust that the lifetime of
the reference returned by the `longest` function is the same as the smaller of
the lifetimes of the references passed in. Therefore, the borrow checker
disallows the code in Listing 10-23 as possibly having an invalid reference.

Try designing more experiments that vary the values and lifetimes of the
references passed in to the `longest` function and how the returned reference
is used. Make hypotheses about whether or not your experiments will pass the
borrow checker before you compile; then check to see if you’re right!
