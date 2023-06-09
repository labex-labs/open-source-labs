# React useComponentDidUpdate Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

This code provides a custom hook called `useComponentDidUpdate` that executes a provided `callback` function whenever a component is updated. Here are the steps that the hook follows:

1. Create a `mounted` variable using the `useRef()` hook. This variable tracks whether the component has been mounted or not.
2. Use the `useEffect()` hook to set the value of `mounted` to `true` the first time the hook is executed.
3. On subsequent hook executions, run the provided `callback` function only if the component has already been mounted.
4. If a second argument `condition` is provided, the hook will only execute if any of its dependencies change.
5. This hook behaves like the `componentDidUpdate()` lifecycle method of class components.

Here is the revised code:

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <App />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
