# Checking for sessionStorage Accessibility

To check if `sessionStorage` is accessible, you can use the following code:

```js
const isSessionStorageEnabled = () => {
  try {
    const key = `__storage__test`;
    window.sessionStorage.setItem(key, null);
    window.sessionStorage.removeItem(key);
    return true;
  } catch (e) {
    return false;
  }
};
```

This code uses a `try...catch` block to test if all operations complete successfully. If `sessionStorage` is accessible, it will return `true`. Otherwise, it will return `false`.

To test storing and deleting a value in `sessionStorage`, the code uses `Storage.setItem()` and `Storage.removeItem()`.

To start practicing coding, open the Terminal/SSH and type `node`.

You can call the `isSessionStorageEnabled()` function to check if `sessionStorage` is enabled. It will return `true` if `sessionStorage` is accessible, and `false` otherwise.
