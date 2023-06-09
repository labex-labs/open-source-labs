# Collapsible Accordion

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

To render an accordion menu with multiple collapsible content elements, you can follow these steps:

1. Define an `AccordionItem` component that renders a `<button>` and updates the component while notifying its parent via the `handleClick` callback.
2. Use the `isCollapsed` prop in `AccordionItem` to determine its appearance and set its `className`.
3. Define an `Accordion` component and use the `useState()` hook to initialize the value of the `bindIndex` state variable to `defaultIndex`.
4. Filter `children` to remove unnecessary nodes, except for `AccordionItem`, by identifying the function's name.
5. Use `Array.prototype.map()` on the collected nodes to render the individual collapsible elements.
6. Define `changeItem`, which will be executed when clicking an `AccordionItem`'s `<button>`.
7. `changeItem` executes the passed callback, `onItemClick`, and updates `bindIndex` based on the clicked element.

Here is the revised code:

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
