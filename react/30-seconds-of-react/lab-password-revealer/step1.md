# Show/Hide Password Toggle

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

The following code renders a password input field with a reveal button. It uses the `useState()` hook to create the `shown` state variable and set its initial value to `false`. When the `Show/Hide` button is clicked, the `setShown` function is called, toggling the `type` of the input between `'text'` and `'password'`.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
