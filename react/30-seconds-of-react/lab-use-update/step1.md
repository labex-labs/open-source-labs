# React useUpdate Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To force a component to re-render when called, use the `useReducer()` hook to create a new object every time it's updated and return its dispatch. Here is an example implementation of `useUpdate()` function:

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

You can then use `useUpdate()` in your component to trigger a re-render when necessary:

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
