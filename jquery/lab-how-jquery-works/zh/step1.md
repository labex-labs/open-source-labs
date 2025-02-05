# jQuery 如何工作

> 虚拟机中已提供 `index.html`。

此文件将在环境初始化期间自动生成。如果未自动生成，请创建该文件并按上图所示编写函数。函数代码如下：

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // 你的代码写在这里。
    </script>
  </body>
</html>
```

`<script>` 元素中的 `src` 属性必须指向 jQuery 的副本。从 [下载 jQuery](https://jquery.com/download/) 页面下载一份 jQuery，并将 `jquery.min.js` 文件存储在与你的 HTML 文件相同的目录中。

> 注意：当你下载 jQuery 时，文件名可能包含版本号，例如 `jquery-x.y.z.js`。确保将此文件重命名为 `jquery.js`，或者更新 `<script>` 元素的 `src` 属性以匹配文件名。

#### 在文档就绪时启动代码

为确保代码在浏览器完成加载文档后运行，许多 JavaScript 程序员将代码包装在 `onload` 函数中：

```js
window.onload = function () {
  alert("welcome");
};
```

不幸的是，代码要等到所有图像（包括横幅广告）都下载完成后才会运行。为了在文档准备好被操作时立即运行代码，jQuery 有一个称为 [就绪事件](http://api.jquery.com/ready/) 的语句：

```js
$(document).ready(function () {
  // 你的代码写在这里。
});
```

> 注意：jQuery 库通过 `window` 对象的两个属性 `jQuery` 和 `$` 来暴露其方法和属性。`$` 只是 `jQuery` 的别名，通常使用它是因为它写起来更短更快。

例如，在就绪事件中，你可以为链接添加一个点击处理程序：

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

将上述 jQuery 代码复制到你的 HTML 文件中 `// 你的代码写在这里` 的位置。然后，保存你的 HTML 文件并在浏览器中重新加载测试页面。

#### 完整示例

以下示例说明了上述讨论的点击处理代码，直接嵌入在 HTML `<body>` 中。请注意，在实际应用中，通常最好将代码放在一个单独的 JS 文件中，并使用 `<script>` 元素的 `src` 属性在页面上加载它。

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>点击我</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> 请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
