# 事件

> 虚拟机中已提供 `index.html`。

网站上真正的交互性需要事件处理程序。这些是代码结构，用于监听浏览器中的活动并相应地运行代码。最明显的例子是处理 [点击事件](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event)，当你用鼠标点击某个东西时，浏览器会触发该事件。要演示这一点，请在控制台中输入以下内容，然后点击当前网页：

```js
document.querySelector("html").addEventListener("click", function () {
  alert("哎哟！别戳我了！");
});
```

有多种方法可以将事件处理程序附加到元素上。
在这里，我们选择了 [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html) 元素。然后我们调用它的 [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) 函数，传入要监听的事件名称 (`'click'`) 和事件发生时要运行的函数。

我们刚刚传递给 `addEventListener()` 的函数称为 _匿名函数_，因为它没有名称。有一种编写匿名函数的替代方法，我们称之为 _箭头函数_。
箭头函数使用 `() =>` 而不是 `function ()`：

```js
document.querySelector("html").addEventListener("click", () => {
  alert("哎哟！别戳我了！");
});
```

> 请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页以预览网页。
