# Controlled Input Field

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Rewritten:

This code snippet provides a controlled `<input>` element that utilizes a callback function to inform its parent about any updates to its value. Here's how it works:

- The controlled input field's value is determined by the `value` prop passed down from the parent.
- Any changes made to the input field by the user are captured by the `onChange` event, which triggers the `onValueChange` callback function and sends the new value back up to the parent component.
- To update the input field's value, the parent must update the `value` prop that it passes down to the controlled input component.

Here's an example implementation of the `ControlledInput` component, followed by a usage example in a `Form` component:

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState('');

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <Form />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
