# React useKeyPress Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Revised:

This function listens for changes in the pressed state of a given key. To use it:

- Call `useKeyPress()` with the target key as an argument.
- `useKeyPress()` returns a boolean value that indicates whether the key is currently pressed.
- The function uses the `useState()` hook to create a state variable that holds the pressed state of the given key.
- It defines two handler functions that update the state variable on key down or key up accordingly.
- The `useEffect()` hook and `EventTarget.addEventListener()` are used to handle the `'keydown'` and `'keyup'` events.
- Finally, `EventTarget.removeEventListener()` is used to perform cleanup after the component is unmounted.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

Here's an example usage of `useKeyPress()` in a React component:

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
