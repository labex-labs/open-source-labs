# React useWindowSize Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To track the dimensions of the browser window, the following steps can be taken:

1. Use the `useState()` hook to initialize a state variable `windowSize` that will hold the window's dimensions. Initialize with both values set to `undefined` to avoid mismatch between server and client renders.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined,
});
```

2. Create a function `handleResize()` that uses `Window.innerWidth` and `Window.innerHeight` to update the state variable. This function will be called whenever the `'resize'` event is triggered.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Use the `useEffect()` hook to set an appropriate listener for the `'resize'` event on mount and clean it up when unmounting.

```jsx
React.useEffect(() => {
  window.addEventListener('resize', handleResize);

  handleResize();

  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []);
```

Putting it all together, the `useWindowSize()` custom hook can be defined as follows:

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined,
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener('resize', handleResize);

    handleResize();

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return windowSize;
};
```

To use the `useWindowSize()` hook, simply call it in a component and destructure the `width` and `height` values from the returned object.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Window size: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <MyApp />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
