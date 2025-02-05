# 添加样式

在 React 中，你使用 `className` 指定 CSS 类。它的工作方式与 HTML 的 [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) 属性相同：

```html
<img className="avatar" />
```

然后你在一个单独的 CSS 文件中为其编写 CSS 规则：

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React 没有规定你如何添加 CSS 文件。在最简单的情况下，你会在 HTML 中添加一个 `<link>` 标签。如果你使用构建工具或框架，请查阅其文档以了解如何将 CSS 文件添加到你的项目中。

```js
// App.js
import "./App.css";
```

你也可以在 JSX 花括号内放入更复杂的表达式，例如 [字符串拼接](https://javascript.info/operators#string-concatenation-with-binary)：

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

在上面的示例中，`style={{}}` 不是特殊语法，而是 `style={ }` JSX 花括号内的常规 `{}` 对象。当你的样式依赖于 JavaScript 变量时，可以使用 `style` 属性。
