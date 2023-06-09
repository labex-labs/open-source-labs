# Uncontrolled Range Input

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a slider in React, use the `Slider` component and pass in the `min`, `max`, `defaultValue`, and `onValueChange` props.

In the `Slider` component, set the `type` of the `<input>` element to `"range"` to create a slider. Use the `defaultValue` prop passed down from the parent as the uncontrolled input field's initial value. Use the `onChange` event to fire the `onValueChange` callback and send the new value to the parent.

Here's the revised code for the `Slider` component:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

To render the `Slider` component, use `ReactDOM.createRoot` and pass in the `onValueChange` callback function:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
