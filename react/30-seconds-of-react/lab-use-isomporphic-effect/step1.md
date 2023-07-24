# React useIsomporphicEffect Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To ensure the proper use of `useEffect()` on the server and `useLayoutEffect()` on the client, you can use `typeof` to check if the `Window` object is defined. If it is, return `useLayoutEffect()`, otherwise return `useEffect()`. Here is an example of how to implement this:

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Then, in your code, you can use `useIsomorphicEffect()` as shown in this example:

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

This will log 'Hello' in the console when the component mounts, and will work correctly on both the server and the client.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
