# Checking for localStorage Accessibility

To check if `localStorage` is accessible, use the following code:

```js
const isLocalStorageEnabled = () => {
  try {
    const key = `__storage__test`;
    window.localStorage.setItem(key, null);
    window.localStorage.removeItem(key);
    return true;
  } catch (e) {
    return false;
  }
};
```

This function uses a `try...catch` block to test if `Storage.setItem()` and `Storage.removeItem()` operations can be performed successfully. If the operations complete successfully, the function returns `true`, indicating that `localStorage` is enabled. If an error is thrown, the function returns `false`, indicating that `localStorage` is not enabled.

To test if `localStorage` is enabled, call the `isLocalStorageEnabled()` function. If it returns `true`, `localStorage` is accessible.
