# 动画完成后执行某些操作

在实现 jQuery 特效时，一个常见的错误是认为链式调用中的下一个方法会等到动画运行完成后才执行。

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

需要注意的是，上面的 `.fadeIn()` 只是启动了动画。一旦启动，动画是通过在 JavaScript 的 `setInterval()` 循环中快速更改 CSS 属性来实现的。当你调用 `.fadeIn()` 时，它启动动画循环，然后返回 jQuery 对象，并将其传递给 `.addClass()`，这样在动画循环刚刚开始时就会添加 `lookAtMe` 样式类。

要将一个操作推迟到动画运行完成之后执行，你需要使用动画回调函数。你可以将动画回调函数作为第二个参数传递给上述任何一个动画方法。对于上面的代码片段，我们可以如下实现回调：

```js
// 淡入所有隐藏的段落；然后给它们添加一个样式类（使用动画回调函数修正）
$("div.hidden").fadeIn(1500, function () {
  // this = 刚刚完成动画的 DOM 元素
  $(this).addClass("lookAtMe");
});
```

请注意，你可以使用关键字 `this` 来引用正在进行动画的 DOM 元素。还要注意，回调函数会为 jQuery 对象中的每个元素调用。这意味着如果你的选择器没有返回任何元素，你的动画回调函数将永远不会运行！你可以通过测试你的选择是否返回了任何元素来解决这个问题；如果没有，你可以直接立即运行回调函数。

```js
// 即使没有元素需要动画处理，也运行回调函数
var someElement = $("#nonexistent");

var cb = function () {
  console.log("完成！");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> 你可以刷新“Web 8080”标签页来预览网页。
