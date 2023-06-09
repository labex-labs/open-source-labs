# React useSearchParam Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Revised:

To track the browser's location search param, use the following steps:

1. Create a callback using the `useCallback()` hook. The callback should use the `URLSearchParams` constructor to get the current value of the desired parameter.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. Create a state variable that holds the current value of the parameter using the `useState()` hook.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. Set appropriate event listeners to update the state variable when mounting and clean them up when unmounting using the `useEffect()` hook.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

Here's an example of how to use this custom hook in a component:

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Post param value: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        View post 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Exit
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

This example creates a `MyApp` component that uses the `useSearchParam` custom hook to track the value of the `post` parameter in the location search. The `post` value is displayed in a paragraph tag. Two buttons are also included to demonstrate how to change the location search parameter value.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
