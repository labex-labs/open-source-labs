# React useHover Hook

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

This code creates a custom hook that handles hovering over a wrapped component.

To use the hook:

- Use `useState()` to create a variable that holds the hovering state.
- Use `useCallback()` to memoize two handler functions that update the state.
- Use `useCallback()` to create a callback ref and create or update the listeners for the `'mouseover'` and `'mouseout'` events.
- Use `useRef()` to keep track of the last node passed to `callbackRef` to be able to remove its listeners.

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

This is an example usage of the hook:

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Hovering" : "Not hovering"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
