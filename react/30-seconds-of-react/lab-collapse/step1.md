# Collapsible Content

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

This function renders a collapsible component with a button that toggles the visibility of its content. Here's how to use it:

1. Use the `useState()` hook to create the `isCollapsed` state variable, which represents whether the content is currently collapsed or expanded. Initialize it to `collapsed`.
2. Use the `<button>` element to toggle the `isCollapsed` state and show/hide the content passed down via the `children` prop.
3. Use `isCollapsed` to apply the appropriate CSS class to the content container, either `collapsed` or `expanded`, which determines its appearance.
4. Update the `aria-expanded` attribute of the content container based on the `isCollapsed` state, to make the component accessible to users with disabilities.

Here's the CSS code needed for this component:

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

And here's the JavaScript code:

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Show" : "Hide"} content
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

To use this component, simply call it with the content you want to collapse:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>This is a collapse</h1>
    <p>Hello world!</p>
  </Collapse>
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
