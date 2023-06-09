# React usePersistedState Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This hook returns a stateful value that is persisted in `localStorage`, along with a function that can be used to update it. To use it, follow these steps:

1. Use the `useState()` hook to initialize the `value` to `defaultValue`.
2. Use the `useRef()` hook to create a ref that will hold the `name` of the value in `Window.localStorage`.
3. Use 3 instances of the `useEffect()` hook for initialization, `value` change, and `name` change respectively.
4. When the component is first mounted, use `Storage.getItem()` to update `value` if there's a stored value, or `Storage.setItem()` to persist the current value.
5. When `value` is updated, use `Storage.setItem()` to store the new value.
6. When `name` is updated, use `Storage.setItem()` to create the new key, update the `nameRef`, and use `Storage.removeItem()` to remove the previous key from `Window.localStorage`.
7. Note that the hook is meant for use with primitive values (i.e. not objects) and doesn't account for changes to `Window.localStorage` due to other code. Both of these issues can be easily handled (e.g. JSON serialization and handling the `'storage'` event).

Here is the updated code:

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
