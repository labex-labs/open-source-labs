# Reorder Function Arguments with Flip

To swap the order of function arguments, use the `flip` function. This function takes a function as an argument and returns a new function that swaps the first and last arguments.

To implement `flip`:

- Use argument destructuring and a closure with variadic arguments.
- Splice the first argument using the spread operator (`...`) to make it the last argument before applying the rest.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

Here's an example of how to use `flip` to reorder the arguments of `Object.assign`:

```js
let a = { name: "John Smith" };
let b = {};

// Create a new function that swaps the arguments of Object.assign
const mergeFrom = flip(Object.assign);

// Create a new function that binds the first argument to a
let mergePerson = mergeFrom.bind(null, a);

// Call the new function with b as the second argument
mergePerson(b); // b is now equal to a

// Alternatively, merge a and b without using the new function
b = {};
Object.assign(b, a); // b is now equal to a
```
