# React useOnWindowScroll Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function executes a callback function every time the window is scrolled. To implement it:

1. Use the `useRef()` hook to create a reference variable, `listener`.
2. Use the `useEffect()` hook and `EventTarget.addEventListener()` to listen to the `'scroll'` event of the `Window` object, and assign the listener reference to `listener.current`.
3. Use `EventTarget.removeEventListener()` to remove any existing listeners when the component unmounts.

Here's the code:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

To test the function, you can use it in a component like this:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

This will log the vertical scroll position of the window every time it's scrolled.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
