# 对象表格视图

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此组件渲染一个表格，其行由对象数组和属性名列表动态创建。要实现这一点：

- 使用 `Object.keys()`、`Array.prototype.filter()`、`Array.prototype.includes()` 和 `Array.prototype.reduce()` 生成一个 `filteredData` 数组，该数组包含所有具有 `propertyNames` 中指定键的对象。
- 渲染一个 `<table>` 元素，其列数等于 `propertyNames` 中的值的数量。
- 使用 `Array.prototype.map()` 将 `propertyNames` 数组中的每个值渲染为一个 `<th>` 元素。
- 使用 `Array.prototype.map()` 将 `filteredData` 数组中的每个对象渲染为一个 `<tr>` 元素，该元素为对象中的每个键包含一个 `<td>`。
- 请注意，此组件不适用于嵌套对象，如果 `propertyNames` 中指定的任何属性内有嵌套对象，它将会出错。

以下是代码：

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

你可以通过传入对象数组和属性名列表来使用该组件：

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
