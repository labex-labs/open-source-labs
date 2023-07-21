# Here's a function to reverse a string:

To reverse a string, use the spread operator (`...`) and `Array.prototype.reverse()`. Combine characters to get a string using `Array.prototype.join()`. Here's the code:

```js
const reverseString = (str) => [...str].reverse().join("");
```

Example usage:

```js
reverseString("foobar"); // 'raboof'
```
