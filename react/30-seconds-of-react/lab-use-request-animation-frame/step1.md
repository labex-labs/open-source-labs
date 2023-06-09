# React useRequestAnimationFrame Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To run an animating function before every repaint, use the `useRef()` hook to create `requestRef` and `previousTimeRef` variables. Then, define an `animate()` function that updates these variables, runs the `callback`, and calls `Window.requestAnimationFrame()` perpetually. Lastly, use the `useEffect()` hook with an empty array to initialize the value of `requestRef` with `Window.requestAnimationFrame()`, and use the returned value and `Window.cancelAnimationFrame()` to clean up when the component unmounts.

Here is an example implementation of `useRequestAnimationFrame()`:

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

To use this custom hook in a component, simply pass a callback function to it. For example, to create a simple counter that updates at 100 FPS:

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
