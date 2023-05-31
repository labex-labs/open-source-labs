# Function to Check if an Object Contains a Specific Value

To check if an object contains a specific value, use the following function:

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

To use this function, pass in the object you want to search and the target value as arguments. The function will return `true` if the object contains the value and `false` if it does not.

Here's an example:

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

To get started with coding, open the Terminal/SSH and type `node`.
