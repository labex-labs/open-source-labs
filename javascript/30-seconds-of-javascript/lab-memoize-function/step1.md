# Memoize Function

To start coding, open the Terminal/SSH and type `node`. This function returns the memoized (cached) function. Here are the steps to use this function:

1. Instantiate a new `Map` object to create an empty cache.
2. Return a function that takes a single argument which will be supplied to the memoized function. Before executing the function, check if the output for that specific input value is already cached. If it is, return the cached output; otherwise, store and return it.
3. Use the `function` keyword to allow the memoized function to have its `this` context changed if necessary.
4. Set the `cache` as a property on the returned function to allow access to it.

Here's the code that implements the memoize function:

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

To see how this function works, you can use it with the `anagrams` function. Here's an example:

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // takes a long time
anagramsCached("javascript"); // returns virtually instantly since it's cached
console.log(anagramsCached.cache); // The cached anagrams map
```
