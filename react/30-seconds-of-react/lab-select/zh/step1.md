# 不受控的选择元素

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这是一个渲染受控 `<select>` 元素的组件。该组件接受一个值数组和一个回调函数，用于将选定的值传递给其父组件。以下是使用此组件的步骤：

- 使用 `selectedValue` 属性设置 `<select>` 元素的初始值。
- 使用 `onValueChange` 属性指定当 `<select>` 元素的值发生变化时应调用的回调函数。
- 对 `values` 数组使用 `Array.prototype.map()` 为每个传递的值创建一个 `<option>` 元素。
- `values` 中的每个项应该是一个包含两个元素的数组，其中第一个元素是该项的 `value`，第二个元素是它的显示文本。

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

以下是使用此组件的示例：

```jsx
const choices = [
  ["grapefruit", "葡萄柚"],
  ["lime", "酸橙"],
  ["coconut", "椰子"],
  ["mango", "芒果"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
