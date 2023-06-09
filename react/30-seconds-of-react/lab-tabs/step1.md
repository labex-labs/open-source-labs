# Tabs

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Here is a revised version of the content:

---

To render a tabbed menu and view component, follow these steps:

1. Define a `Tabs` component. Use the `useState()` hook to set the `bindIndex` state variable to `defaultIndex`.
2. Define a `TabItem` component and filter the `children` passed to the `Tabs` component to remove any unnecessary nodes except for `TabItem`. You can do this by identifying the function's name.
3. Define a function called `changeTab`. This function will be executed when a user clicks a `<button>` from the menu.
4. `changeTab` executes the passed callback, `onTabClick`, and updates `bindIndex` based on the clicked element.
5. Use `Array.prototype.map()` on the collected nodes to render the menu and view of the tabs.
6. Use the value of `bindIndex` to determine the active tab and apply the correct `className`.

Here is the CSS code to style the tabbed menu and view:

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

Here is the updated JavaScript code to implement the `Tabs` component:

```jsx
const TabItem = props => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
  
  const changeTab = newIndex => {
    if (typeof onTabClick === 'function') onTabClick(newIndex);
    setBindIndex(newIndex);
  };
  
  const items = children.filter(item => item.type.name === 'TabItem');

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? 'focus' : ''}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? 'selected' : ''
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

Finally, here is an example of how to use the `Tabs` component:

```jsx
ReactDOM.createRoot(document.getElementById('root')).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
