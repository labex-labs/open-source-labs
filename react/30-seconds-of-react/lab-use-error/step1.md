# React useError Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Here's a revised version of the content:

---

This code creates an error dispatcher. It uses three React hooks to manage the error state and dispatch it to the user interface.

Here's how the code works:

1. The `useState()` hook creates a state variable called `error` that holds the error object. It takes an initial value of `err`, which is passed in as an argument to the hook.

2. The `useEffect()` hook is used to "throw" the error whenever it's truthy. This hook takes a function and an array of dependencies as arguments. In this case, the function checks if the `error` state variable is truthy (i.e. not null, undefined, 0, false, or an empty string), and throws it if it is. The array of dependencies is `[error]`, which means the effect will be re-run whenever the `error` variable changes.

3. The `useCallback()` hook is used to create a cached function called `dispatchError`, which updates the `error` state variable and returns the new function. This hook takes a function and an array of dependencies as arguments. In this case, the function takes an argument `err`, which is the new error object to be dispatched. The array of dependencies is `[]`, which means the cached function will only be re-created if the component is re-rendered.

Here's an example of how to use the `useError()` hook in a component:

1. Create a new component called `ErrorButton`.

2. Inside the component, call the `useError()` hook to get the `dispatchError` function.

3. Create a click handler function called `clickHandler` that calls `dispatchError` with a new error object.

4. Render a button that calls `clickHandler` when clicked.

Here's the revised code:

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback(
    (err) => {
      setError(err);
    },
    []
  );

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error('Error!'));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <ErrorButton />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
