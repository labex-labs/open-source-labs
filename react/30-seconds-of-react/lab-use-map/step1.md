# React useMap Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Refactored:

- The `useMap()` hook creates a stateful `Map` object and a set of functions to manipulate it using React hooks.
- The `useState()` hook initializes the `Map` state with the `initialValue`.
- The `useMemo()` hook creates a set of non-mutating actions that manipulate the `map` state variable using the state setter to create a new `Map` every time.
- The `useMap()` hook returns an array containing the `map` state variable and the created `actions`.
- The `MyApp` component uses the `useMap()` hook to initialize the stateful `Map` object and provides buttons to add, reset, and remove items from the `Map`.
- The `JSON.stringify()` function formats the `Map` object into a readable JSON string.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map()),
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
