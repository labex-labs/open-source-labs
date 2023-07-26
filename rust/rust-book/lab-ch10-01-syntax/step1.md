# Removing Duplication by Extracting a Function

Generics allow us to replace specific types with a placeholder that represents
multiple types to remove code duplication. Before diving into generics syntax,
let’s first look at how to remove duplication in a way that doesn’t involve
generic types by extracting a function that replaces specific values with a
placeholder that represents multiple values. Then we’ll apply the same
technique to extract a generic function! By looking at how to recognize
duplicated code you can extract into a function, you’ll start to recognize
duplicated code that can use generics.

We’ll begin with the short program in Listing 10-1 that finds the largest
number in a list.

Filename: `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-1: Finding the largest number in a list of numbers

We store a list of integers in the variable `number_list` [1] and place a
reference to the first number in the list in a variable named `largest` [2]. We
then iterate through all the numbers in the list [3], and if the current number
is greater than the number stored in `largest` [4], we replace the reference in
that variable [5]. However, if the current number is less than or equal to the
largest number seen so far, the variable doesn’t change, and the code moves on
to the next number in the list. After considering all the numbers in the list,
`largest` should refer to the largest number, which in this case is 100.

We’ve now been tasked with finding the largest number in two different lists of
numbers. To do so, we can choose to duplicate the code in Listing 10-1 and use
the same logic at two different places in the program, as shown in Listing 10-2.

Filename: `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-2: Code to find the largest number in _two_ lists of numbers

Although this code works, duplicating code is tedious and error prone. We also
have to remember to update the code in multiple places when we want to change
it.

To eliminate this duplication, we’ll create an abstraction by defining a
function that operates on any list of integers passed in a parameter. This
solution makes our code clearer and lets us express the concept of finding the
largest number in a list abstractly.

In Listing 10-3, we extract the code that finds the largest number into a
function named `largest`. Then we call the function to find the largest number
in the two lists from Listing 10-2. We could also use the function on any other
list of `i32` values we might have in the future.

Filename: `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

Listing 10-3: Abstracted code to find the largest number in two lists

The `largest` function has a parameter called `list`, which represents any
concrete slice of `i32` values we might pass into the function. As a result,
when we call the function, the code runs on the specific values that we pass in.

In summary, here are the steps we took to change the code from Listing 10-2 to
Listing 10-3:

1. Identify duplicate code.
1. Extract the duplicate code into the body of the function, and specify the
   inputs and return values of that code in the function signature.
1. Update the two instances of duplicated code to call the function instead.

Next, we’ll use these same steps with generics to reduce code duplication. In
the same way that the function body can operate on an abstract `list` instead
of specific values, generics allow code to operate on abstract types.

For example, say we had two functions: one that finds the largest item in a
slice of `i32` values and one that finds the largest item in a slice of `char`
values. How would we eliminate that duplication? Let’s find out!
