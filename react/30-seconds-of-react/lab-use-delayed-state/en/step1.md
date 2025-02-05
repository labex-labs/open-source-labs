# React useDelayedState Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To delay the creation of a stateful value until a condition is met, follow these steps:

1. Use the `useState()` hook to create a stateful value containing the actual `state` and a boolean, `loaded`.
2. Use the `useEffect()` hook to update the stateful value if the `condition` or `loaded` changes.
3. Create a function, `updateState`, that only updates the `state` value if `loaded` is truthy.

```jsx
const useDelayedState = (initialState, condition) => {
  const [{ state, loaded }, setState] = React.useState({
    state: null,
    loaded: false
  });

  React.useEffect(() => {
    if (!loaded && condition) setState({ state: initialState, loaded: true });
  }, [condition, loaded]);

  const updateState = (newState) => {
    if (!loaded) return;
    setState({ state: newState, loaded });
  };

  return [state, updateState];
};
```

Here's an example of how to use the `useDelayedState` hook:

```jsx
const App = () => {
  const [branches, setBranches] = React.useState([]);
  const [selectedBranch, setSelectedBranch] = useDelayedState(
    branches[0],
    branches.length
  );

  React.useEffect(() => {
    const handle = setTimeout(() => {
      setBranches(["master", "staging", "test", "dev"]);
    }, 2000);
    return () => {
      handle && clearTimeout(handle);
    };
  }, []);

  return (
    <div>
      <p>Selected branch: {selectedBranch}</p>
      <select onChange={(e) => setSelectedBranch(e.target.value)}>
        {branches.map((branch) => (
          <option key={branch} value={branch}>
            {branch}
          </option>
        ))}
      </select>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
