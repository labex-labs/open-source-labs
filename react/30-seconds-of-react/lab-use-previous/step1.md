# React usePrevious Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To store the previous state or props, you can create a custom hook. Here are the steps:

1. Define a custom hook that takes a `value` argument.
2. Use the `useRef()` hook to create a `ref` for the `value`.
3. Use the `useEffect()` hook to remember the latest `value`.
4. Return the `ref.current` value.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

Here's an example of using the `usePrevious` hook:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Current: {value} - Previous: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

The `Counter` component displays the current and previous values of `value`. When the `Increment` button is clicked, `value` is updated and the previous value is stored using the `usePrevious` hook.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
