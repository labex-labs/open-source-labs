# Uncontrolled Input Field

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

This code renders an uncontrolled `<input>` element that uses a callback function to inform its parent about value updates. To use it:

- Pass the initial value down from the parent using the `defaultValue` prop.
- Pass a callback function called `onValueChange` to handle value updates.
- Use the `onChange` event to fire the callback and send the new value to the parent.

Here's an example:

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
