# Checking if Environment is a Browser

To check if the current runtime environment is a browser, use the `Array.prototype.includes()` method on the `typeof` values of both `Window` and `Document`. These globals are usually only available in a browser environment unless they were explicitly defined. This method will return `true` if one of them is `undefined`. The `typeof` allows checking for the existence of globals without throwing a `ReferenceError`. If both of them are not `undefined`, then the current environment is assumed to be a browser.

Use the following code to determine if the current environment is a browser:

```js
const isBrowser = () => ![typeof window, typeof document].includes("undefined");
```

When you call `isBrowser()`, it will return `true` if the environment is a browser and `false` if it is Node.
