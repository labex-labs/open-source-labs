# How to Generate a Random Number in a Given Range using JavaScript

To generate a random number in a specified range using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Math.random()` method to generate a random value.
3. Map the generated value to the desired range using multiplication.
4. Use the following code to create a function that generates a random number in the given range:

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5. To use the function, pass in the minimum and maximum values of the desired range as arguments. For example:

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

By following these steps, you can easily generate a random number in a given range using JavaScript.
