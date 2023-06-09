# React useOnGlobalEvent Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function executes a callback function whenever an event occurs on the global object. To implement this function:

1. Use the `useRef()` hook to create a variable, `listener`, which will hold the listener reference.
2. Use the `useRef()` hook to create a variable that will hold the previous values of the `type` and `options` arguments.
3. Use the `useEffect()` hook and `EventTarget.addEventListener()` to listen to the given event `type` on the `Window` global object.
4. Use `EventTarget.removeEventListener()` to remove any existing listeners and clean up when the component unmounts.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Here's an example of how to use this function:

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
