# React useTimeout Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To implement `setTimeout()` in a declarative manner, create a custom hook that takes a `callback` and a `delay`. Use the `useRef()` hook to create a `ref` for the callback function, and use the `useEffect()` hook to remember the latest callback. Then, use the `useEffect()` hook to set up the timeout and clean up. 

Here is an example code snippet that demonstrates this approach:

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = props => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <OneSecondTimer />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
