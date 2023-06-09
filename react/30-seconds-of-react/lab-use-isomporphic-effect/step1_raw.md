# React useIsomporphicEffect Hook

Resolves to `useEffect()` on the server and `useLayoutEffect()` on the client.

- Use `typeof` to check if the `Window` object is defined. If it is, return the `useLayoutEffect()`. Otherwise return `useEffect()`.

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```
