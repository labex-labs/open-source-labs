# React useHash Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Revised:

This code tracks and updates the browser's location hash value. To use it, follow these steps:

1. Use the `useState()` hook to lazily get the `hash` property of the `Location` object.
2. Use the `useCallback()` hook to create a handler that updates the `hash` state when the `'hashchange'` event is fired.
3. Use the `useEffect()` hook to add a listener for the `'hashchange'` event when mounting and clean it up when unmounting.
4. Use the `useCallback()` hook to create a function that updates the `hash` property of the `Location` object with the given value.
5. In your component, call `useHash()` to get the current `hash` value and an `updateHash()` function to change it.
6. Use the `updateHash()` function to change the `hash` value.
7. Render the current `hash` value in a component.
8. Create an input field that allows the user to change the `hash` value.

Here's the updated code:

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Current hash value: {hash}</p>
      <p>Edit hash: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
