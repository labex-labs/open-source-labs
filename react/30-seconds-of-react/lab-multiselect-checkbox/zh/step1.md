# 支持多项选择的有状态复选框

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码呈现了一个复选框列表，并使用回调函数将选定的值发送到父组件。以下是创建它的步骤：

1. 使用 `useState()` 钩子，用 `options` 属性初始化 `data` 状态变量。
2. 创建一个 `toggle` 函数，用选定的选项更新 `data` 状态变量，并使用它们调用 `onChange` 回调函数。
3. 映射 `data` 状态变量，以生成各个复选框及其标签。将 `toggle` 函数绑定到每个复选框的 `onClick` 处理程序。

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
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

以下是使用它的示例：

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

请点击右下角的“Go Live”，在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
