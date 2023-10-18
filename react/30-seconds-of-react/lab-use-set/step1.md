# React useSet Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function creates a `Set` object with state and a set of functions that can manipulate the state.

To use this function:

- Call `useState()` and the `Set` constructor to create a new `Set` from the `initialValue`.
- Use `useMemo()` to create a set of non-mutating functions that can manipulate the `set` state variable. Use the state setter to create a new `Set` every time.
- Return both the `set` state variable and the created `actions`.

Here's an example implementation of this function:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

Here's an example usage of this function:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Add</button>
      <button onClick={() => clear()}>Reset</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
