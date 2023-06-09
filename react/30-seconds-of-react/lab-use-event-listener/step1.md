# React useEventListener Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

This function adds an event listener for the specified event type on the given element. To use this function, follow these steps:

1. Use the `useRef()` hook to create a ref that will hold the `handler`.
2. Use the `useEffect()` hook to update the value of the `savedHandler` ref any time the `handler` changes.
3. Use the `useEffect()` hook to add an event listener to the given element and clean up when unmounting.
4. Omit the last argument, `el`, to use the `Window` by default.

Here's the revised code:

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = e => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

And here's an example usage of the `useEventListener()` function:

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener('mousemove', updateCoords);

  return (
    <p>Mouse coordinates: {coords.x}, {coords.y}</p>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <MyApp />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
