# Instructions for calculating the midpoint between two pairs of (x,y) points:

To calculate the midpoint between two pairs of (x,y) points, follow these steps:

1. Destructure the array to get `x1`, `y1`, `x2` and `y2`.
2. Calculate the midpoint for each dimension by dividing the sum of the two endpoints by `2`.

Here's an example code snippet that implements the midpoint calculation function:

```js
const midpoint = ([x1, y1], [x2, y2]) => [(x1 + x2) / 2, (y1 + y2) / 2];
```

You can call the `midpoint` function with the following parameters to get the midpoint coordinates:

```js
midpoint([2, 2], [4, 4]); // [3, 3]
midpoint([4, 4], [6, 6]); // [5, 5]
midpoint([1, 3], [2, 4]); // [1.5, 3.5]
```

# Getting started with coding:

To start practicing coding, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start the Node.js environment.
