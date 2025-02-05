# React useSSR Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To check if the code is running on a browser or server, create a custom hook that uses `typeof`, `Window`, `Window.document`, and `Document.createElement()` to determine if the DOM is available. Use the `useState()` hook to define the `inBrowser` state variable and the `useEffect()` hook to update it and clean up at the end. Use the `useMemo()` hook to memoize the return values of the custom hook.

Here is the code:

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return <p>{isBrowser ? "Running on browser" : "Running on server"}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
