# React useSessionStorage Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a stateful value that is persisted to `sessionStorage`, and a function to update it, follow these steps:

1. Use the `useState()` hook with a function to initialize its value lazily.
2. Use a `try...catch` block and `Storage.getItem()` to try and get the value from `Window.sessionStorage`. If no value is found, use `Storage.setItem()` to store the `defaultValue` and use it as the initial state. If an error occurs, use `defaultValue` as the initial state.
3. Define a function that will update the state variable with the passed value and use `Storage.setItem()` to store it.

Here is an example implementation:

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

You can use this hook in your app like this:

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
