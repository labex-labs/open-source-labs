# 将事件扩展到新的页面元素

需要注意的是，`.on()` 只能在设置监听器时已存在的元素上创建事件监听器。例如：

```js
$(document).ready(function () {
  // 现在创建一个带有 alert 类的新按钮元素。
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // 为执行该指令时 DOM 中存在的所有带有 alert 类的按钮元素设置点击行为
  $("button.alert").on("click", function () {
    console.log("一个带有 alert 类的按钮被点击了！");
  });
});
```

如果在设置事件监听器之后创建了类似的元素，它们不会自动获得你之前设置的事件行为。

> 你可以刷新“Web 8080”标签页来预览网页。
