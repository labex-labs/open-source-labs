# React useComponentWillUnmount Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To execute a callback immediately before a component is unmounted and destroyed, you can use the `useEffect()` hook with an empty array as the second argument. Return the provided callback to be executed only once before cleanup. This behavior is similar to the `componentWillUnmount()` lifecycle method of class components. You can also use the following code snippet to create a custom hook `useComponentWillUnmount()` that takes an `onUnmountHandler` function as an argument and executes it before the component is unmounted:

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    [],
  );
};
```

You can then use this custom hook in your functional component like this:

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

This will log "Component will unmount" to the console when the component is about to be unmounted.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
