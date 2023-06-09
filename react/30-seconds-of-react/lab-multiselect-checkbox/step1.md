# Stateful Checkbox With Multiple Selection

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

This code renders a list of checkboxes and sends the selected value(s) to the parent component using a callback function. Here are the revised steps to create it:

1. Use the `useState()` hook to initialize the `data` state variable with the `options` prop.
2. Create a `toggle` function that updates the `data` state variable with the selected option(s) and calls the `onChange` callback function with them.
3. Map the `data` state variable to generate individual checkboxes and their labels. Bind the `toggle` function to the `onClick` handler of each checkbox.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked,
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Here is an example of how to use it:

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
