# 标签

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要渲染一个标签式菜单和视图组件，请执行以下步骤：

1. 定义一个 `Tabs` 组件。使用 `useState()` 钩子将 `bindIndex` 状态变量设置为 `defaultIndex`。
2. 定义一个 `TabItem` 组件，并过滤传递给 `Tabs` 组件的 `children`，以删除除 `TabItem` 之外的任何不必要的节点。你可以通过识别函数的名称来做到这一点。
3. 定义一个名为 `changeTab` 的函数。当用户点击菜单中的 `<button>` 时，此函数将被执行。
4. `changeTab` 执行传递的回调函数 `onTabClick`，并根据点击的元素更新 `bindIndex`。
5. 对收集到的节点使用 `Array.prototype.map()` 来渲染标签的菜单和视图。
6. 使用 `bindIndex` 的值来确定活动标签，并应用正确的 `className`。

以下是为标签式菜单和视图设置样式的 CSS 代码：

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

以下是实现 `Tabs` 组件的 JavaScript 代码：

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
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
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

最后，以下是如何使用 `Tabs` 组件的示例：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
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

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签以预览网页。
