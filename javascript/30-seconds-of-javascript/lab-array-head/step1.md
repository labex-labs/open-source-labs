# How to Get the First Element of an Array in JavaScript

To get the first element of an array in JavaScript, you can use the `head` function. Here's how you can use it:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Use the following code to get the head of an array:

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. Call the `head` function with an array as its argument to get the first element. If the array is empty or falsy, the function will return `undefined`.

Here are some examples:

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
