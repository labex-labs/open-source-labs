# 显示数据

JSX 允许你将标记放入 JavaScript 中。花括号允许你 “逃回” JavaScript，这样你就可以嵌入代码中的一些变量并显示给用户。例如，这将显示 `user.name`：

```js
// App.js
const user = {
  name: "Hedy Lamarr"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
    </>
  );
}
```

你也可以从 JSX 属性 “逃入 JavaScript”，但你必须使用花括号而不是引号。例如，`className="avatar"` 将 `"avatar"` 字符串作为 CSS 类传递，但 `src={user.imageUrl}` 读取 JavaScript `user.imageUrl` 变量的值，然后将该值作为 `src` 属性传递：

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img className="avatar" src={user.imageUrl} />
    </>
  );
}
```
