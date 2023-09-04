# Tooltip

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Here's a clearer, more concise, and more coherent version of the content:

---

This code creates a tooltip component. To use it, do the following:

1. Use the `useState()` hook to create the `show` variable and set it to `false`.
2. Render a container element that contains the tooltip element and the `children` passed to the component.
3. Handle the `onMouseEnter` and `onMouseLeave` events by toggling the `className` of the tooltip, which is controlled by the `show` variable.

Here's the code for the tooltip component:

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

To use the tooltip component, call `ReactDOM.createRoot()` with the following code:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>,
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
