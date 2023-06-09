# React useInterval Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To implement `setInterval()` in a declarative manner, you can create a custom hook that takes a `callback` and a `delay`. The first step is to use the `useRef()` hook to create a `ref` for the callback function. Then, use a `useEffect()` hook to remember the latest `callback` whenever it changes. Finally, use a `useEffect()` hook dependent on `delay` to set up the interval and clean up.

Here's an example code snippet for the custom hook:

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

You can then use this custom hook in your components. For example, to create a timer that updates every second:

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
