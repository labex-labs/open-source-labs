# Generating Gaussian Random Numbers using Box-Muller Transform

To generate Gaussian (normally distributed) random numbers using Box-Muller transform, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the provided code snippet that utilizes the Box-Muller transform to generate random numbers with a Gaussian distribution.
3. The `randomGauss()` function provided in the code snippet generates a random number with a Gaussian distribution.
4. The output of `randomGauss()` function is a number between 0 and 1.
5. The output can be used for various applications, such as statistical simulations, data analysis, and machine learning.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

Example Usage:

```js
randomGauss(); // 0.5
```
