# React useLocalStorage Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Rewritten:

This function creates a value that is saved to `localStorage` and a function to modify it. Here's how it works:

1. To create the value, use the `useState()` hook with a function to initialize it lazily.
2. To retrieve the saved value from `localStorage`, use a `try...catch` block and `Storage.getItem()`. If there's no saved value, use `Storage.setItem()` to store the `defaultValue` and use it as the initial state. If there's an error, use `defaultValue`.
3. Define a function that updates the state variable with the passed value and uses `Storage.setItem()` to save it.

Here's the code:

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

You can use this function in your app like this:

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
