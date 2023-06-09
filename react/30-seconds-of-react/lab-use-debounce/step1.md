# React useDebounce Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To debounce a given value, you can create a custom hook that takes a `value` and a `delay`. Use the `useState()` hook to store the debounced value, and the `useEffect()` hook to update the debounced value every time `value` is updated. To delay invoking the setter of the previous state variable by `delay` ms, use `setTimeout()`. To clean up when dismounting the component, use `clearTimeout()`. This is particularly useful when dealing with user input.

Here is an example implementation of the `useDebounce()` hook:

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

You can use the `useDebounce()` hook in a component like this:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Current: {value} - Debounced: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
