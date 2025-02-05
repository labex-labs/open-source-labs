# Converting Generator Output to Array

To convert the output of a generator function to an array, use the spread operator (`...`). To start practicing coding, open the Terminal/SSH and type `node`.

Here's an example function that converts a generator to an array:

```js
const generatorToArray = (gen) => [...gen];
```

You can use this function as follows:

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
