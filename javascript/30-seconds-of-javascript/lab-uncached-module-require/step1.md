# How to Load an Uncached Module in Node.js

If you want to load a module in Node.js after removing it from the cache (if it exists), you can follow these steps:

1. Open the Terminal or SSH.
2. Type `node` to start coding.
3. Use the `delete` keyword to remove the module from the cache (if it exists).
4. Use `require()` to load the module again.

Here's an example of how to define a function to load an uncached module in Node.js:

```js
const requireUncached = (module) => {
  delete require.cache[require.resolve(module)];
  return require(module);
};
```

To use this function, simply pass the name of the module you want to load as a parameter:

```js
const fs = requireUncached("fs"); // 'fs' will be loaded fresh every time
```
