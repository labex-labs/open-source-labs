# Uncontrolled Select Element

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This is a component that renders a controlled `<select>` element. The component accepts an array of values and a callback function to pass the selected value to its parent component. Here are the steps to use this component:

- Use the `selectedValue` prop to set the initial value of the `<select>` element.
- Use the `onValueChange` prop to specify the callback function that should be called when the value of the `<select>` element changes.
- Use `Array.prototype.map()` on the `values` array to create an `<option>` element for each passed value.
- Each item in `values` should be a 2-element array, where the first element is the `value` of the item and the second one is the displayed text for it.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Here's an example of how to use this component:

```jsx
const choices = [
  ["grapefruit", "Grapefruit"],
  ["lime", "Lime"],
  ["coconut", "Coconut"],
  ["mango", "Mango"],
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />,
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
