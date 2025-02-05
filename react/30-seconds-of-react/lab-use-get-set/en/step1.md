# React useGetSet Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code snippet defines a custom React hook called `useGetSet` that creates a stateful value and returns a pair of functions for getting and setting its value. The `Counter` component uses this hook to implement a delayed increment of a count displayed in a button.

```jsx
const useGetSet = (initialState) => {
  const stateRef = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}), {});

  const getState = React.useCallback(() => stateRef.current, []);
  const setState = React.useCallback((newState) => {
    stateRef.current = newState;
    update();
  }, []);

  return [getState, setState];
};

const Counter = () => {
  const [getCount, setCount] = useGetSet(0);
  const onClick = React.useCallback(() => {
    setTimeout(() => {
      setCount(getCount() + 1);
    }, 1000);
  }, [getCount, setCount]);

  return <button onClick={onClick}>Count: {getCount()}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
