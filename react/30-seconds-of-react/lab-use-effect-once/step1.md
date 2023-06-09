# React useEffectOnce Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

The code below implements a function `useEffectOnce(callback, when)` that runs a `callback` only once when a `when` condition becomes true.

To implement this function:

- Create a variable `hasRunOnce` using the `useRef()` hook to keep track of the execution status of the effect.
- Use the `useEffect()` hook that runs only when the `when` condition changes.
- Inside the `useEffect()` hook, check if `when` is `true` and the effect has not executed before. If both are `true`, run `callback` and set `hasRunOnce` to `true`.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

Here's an example usage of `useEffectOnce()`:

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

In the example, `useEffectOnce()` is used to log "mounted" to the console when the button is clicked for the first time. The `useEffectOnce()` hook is passed two arguments: the `callback` to run and the `when` condition to check. The `when` condition is set to the `clicked` state, so the `callback` runs only when `clicked` is `true` for the first time.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
