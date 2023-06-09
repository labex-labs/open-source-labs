# Toggle

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To render a toggle component, follow these steps:

1. Use the `useState()` hook to initialize the `isToggledOn` state variable to `defaultToggled`.
2. Render an `<input>` element and bind its `onClick` event to update the `isToggledOn` state variable. Apply the appropriate `className` to the wrapping `<label>` element.
3. Use the following CSS to style the toggle component:

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Here's the revised code:

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? 'ON' : 'OFF'}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <Toggle />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
