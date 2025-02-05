# React useForm 钩子

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要从表单字段创建有状态值，你可以使用 `useState()` 钩子为表单中的值创建一个状态变量。然后，创建一个函数，该函数根据表单字段触发的适当事件来更新状态变量。

以下是一个示例实现：

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

在上述示例中，`useForm()` 接受一个初始状态对象，使用 `useState()` 创建一个状态变量 `values`，并返回一个包含 `values` 和一个根据传递给它的事件更新 `values` 的函数的数组。

你可以在表单组件中像这样使用 `useForm()`：

```jsx
const Form = () => {
  const initialState = { email: "", password: "" };
  const [values, setValues] = useForm(initialState);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" onChange={setValues} />
      <input type="password" name="password" onChange={setValues} />
      <button type="submit">提交</button>
    </form>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

在 `Form` 组件中，使用初始状态对象调用 `useForm()`，并返回一个包含 `values` 和 `setValues()` 的数组。`handleSubmit()` 函数在表单提交时将 `values` 对象记录到控制台。`input` 元素设置为使用 `setValues()` 函数更新表单值。

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
