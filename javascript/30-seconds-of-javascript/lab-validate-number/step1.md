# Number Validation Function

To validate if a given input is a number, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `parseFloat()` to try to convert the input to a number.
- Use `Number.isNaN()` and logical not (`!`) operator to check if the input is a number.
- Use `Number.isFinite()` to check if the input is finite.
- Use `Number` and the loose equality operator (`==`) to check if the coercion holds.

Here's the code for the `validateNumber` function:

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

You can use the `validateNumber` function as follows:

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
