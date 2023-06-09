# React useOnWindowResize Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code executes a callback function every time the window is resized. To implement it, you should follow these steps:

1. Create a variable called `listener` using the `useRef()` hook. This variable will store the reference to the listener.

2. Use the `useEffect()` hook and `EventTarget.addEventListener()` to listen to the `'resize'` event of the `Window` global object. When the event is triggered, call the `callback` function.

3. Clean up by removing any existing listeners with `EventTarget.removeEventListener()` when the component unmounts.

Here's the revised code:

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Window size: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Resize the window and check the console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
