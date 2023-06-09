# React useDefault Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Refactored code:

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

To create a stateful value with a default fallback, use the `useState()` hook in React. Check if the initial value is either `null` or `undefined`. If it is, return the `defaultState` instead, otherwise return the actual `value` state and the `setValue` function. The refactored code above shows how to implement this functionality in a custom hook called `useDefault`.

In the example provided, `useDefault` is used to create a `user` state with a default value of `{ name: 'Adam' }`. The initial state is set to `{ name: 'John' }`. In the `UserCard` component, `user` is displayed along with an input field to update its name. A clear button is also provided to reset the state to `null`. Finally, the component is rendered using `ReactDOM.createRoot()`.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
