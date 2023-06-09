# React useUnload Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Revised:

The `beforeunload` window event can be handled using the following steps:

1. Create a ref for the callback function, `fn`, using the `useRef()` hook.
2. Use the `useEffect()` hook and `EventTarget.addEventListener()` to handle the `'beforeunload'` event, which is triggered when the user is about to close the window.
3. Use `EventTarget.removeEventListener()` to perform cleanup after the component is unmounted.

Here's the code:

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
