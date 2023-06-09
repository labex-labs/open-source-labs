# React useMediaQuery Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Revised:

This function checks if the current environment matches a given media query and returns the appropriate value.

- First, check if `Window` and `Window.matchMedia()` exist. If not (e.g. in an SSR environment or unsupported browser), return `whenFalse`.
- Use `Window.matchMedia()` to match the given `query`. Cast its `matches` property to a boolean and store it in a state variable, `match`, using the `useState()` hook.
- Use the `useEffect()` hook to add a listener for changes and to clean up the listeners after the hook is destroyed.
- Finally, return either `whenTrue` or `whenFalse` based on the value of `match`.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Less than 400px wide",
    "More than 400px wide"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
