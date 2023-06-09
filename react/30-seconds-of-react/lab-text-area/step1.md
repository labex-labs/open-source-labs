# Uncontrolled Textarea Element

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This function renders a `<textarea>` element that is not controlled by the parent component. It uses a callback function to pass the value of the input to the parent component.

To use this function:

- Pass the `defaultValue` prop from the parent component as the initial value of the input field.
- Use the `onChange` event to trigger the `onValueChange` callback and send the new value to the parent.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Example usage:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
