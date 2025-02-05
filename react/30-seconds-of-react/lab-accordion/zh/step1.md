# 可折叠手风琴

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

要渲染一个带有多个可折叠内容元素的手风琴菜单，你可以按照以下步骤操作：

1. 定义一个 `AccordionItem` 组件，该组件渲染一个 `<button>`，并在通过 `handleClick` 回调通知其父组件的同时更新组件。
2. 在 `AccordionItem` 中使用 `isCollapsed` 属性来确定其外观并设置其 `className`。
3. 定义一个 `Accordion` 组件，并使用 `useState()` 钩子将 `bindIndex` 状态变量的值初始化为 `defaultIndex`。
4. 通过识别函数名称来过滤 `children`，以删除不必要的节点，`AccordionItem` 除外。
5. 对收集到的节点使用 `Array.prototype.map()` 来渲染各个可折叠元素。
6. 定义 `changeItem`，它将在点击 `AccordionItem` 的 `<button>` 时执行。
7. `changeItem` 执行传递的回调 `onItemClick`，并根据点击的元素更新 `bindIndex`。

以下是代码：

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

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
