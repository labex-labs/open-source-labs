# React useComponentDidMount Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To execute a callback function immediately after a component is mounted, you can use the `useEffect()` hook with an empty array as the second argument. This will ensure that the provided callback is executed only once when the component is mounted. The `useComponentDidMount()` function shown below uses this hook to implement the same behavior as the `componentDidMount()` lifecycle method of class components.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
