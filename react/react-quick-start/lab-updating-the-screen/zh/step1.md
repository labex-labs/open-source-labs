# 更新屏幕

> 虚拟机中已提供 React 项目。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

通常，你会希望组件能够 “记住” 某些信息并显示出来。例如，你可能想要统计按钮被点击的次数。为此，需要向组件添加状态。

首先，从 React 中导入 `useState`：

```js
import { useState } from "react";
```

现在，你可以在组件内部声明一个状态变量：

```js
function MyButton() {
  const [count, setCount] = useState(0);
  //...
```

通过 `useState`，你将获得两件事：当前状态（`count`）和用于更新状态的函数（`setCount`）。你可以给它们取任何名字，但惯例是写成 `[something, setSomething]`。

首次显示按钮时，`count` 将为 `0`，因为你将 `0` 传递给了 `useState()`。当你想要更改状态时，调用 `setCount()` 并向其传递新值。点击此按钮将增加计数器的值：

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React 将再次调用你的组件函数。这一次，`count` 将为 `1`。然后将为 `2`，依此类推。

如果你多次渲染同一个组件，每个组件都会有自己的状态。分别点击每个按钮：

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

请注意，每个按钮如何 “记住” 自己的 `count` 状态，并且不会影响其他按钮。

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页来预览网页。

```bash
npm start
```
