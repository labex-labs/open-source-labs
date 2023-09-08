# React usePortal Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a portal that renders children outside the parent component, follow these steps:

1. Use the `useState()` hook to create a state variable that holds the `render()` and `remove()` functions for the portal.
2. Use `ReactDOM.createPortal()` and `ReactDOM.unmountComponentAtNode()` to create a portal and a function to remove it. Use the `useCallback()` hook to wrap and memoize these functions as `createPortal()`.
3. Use the `useEffect()` hook to call `createPortal()` and update the state variable any time `el`'s value changes.
4. Finally, return the `render()` function of the state variable.

Here's an example implementation:

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

To use this hook, create a component that calls `usePortal()` with the desired DOM element as an argument. This component can then use the returned `render()` function to render content in the portal:

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
