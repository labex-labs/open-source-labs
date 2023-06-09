# React useMergeState Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a stateful value and a function to update it by merging the new state provided, use the `useState()` hook to create a state variable and initialize it to `initialState`. Create a function that will update the state variable by merging the new state provided with the existing one. If the new state is a function, call it with the previous state as the argument and use the result. If no argument is provided, the state variable will be initialized with an empty object (`{}`). The following code demonstrates how to implement this using the `useMergeState` custom hook:

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

Here is an example usage of the `useMergeState` hook in a component named `MyApp`:

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
