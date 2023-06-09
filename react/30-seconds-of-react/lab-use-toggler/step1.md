# React useToggler Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To create a boolean state variable that can be toggled between its two states, follow these steps:

1. Use the `useState()` hook to create the `value` state variable and its setter.
2. Create a function that toggles the value of the `value` state variable and memoize it, using the `useCallback()` hook.
3. Return the `value` state variable and the memoized toggler function.

Here is an example implementation:

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

You can then use this hook in your components, like this:

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
