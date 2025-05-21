# 理解 HTML 结构

在开始创建动画之前，你需要了解我们将使用的 HTML 结构。在这一步中，我们将检查提供的 HTML 文件并进行必要的修改。

1. 在编辑器中打开 `index.html` 文件。

2. 如果文件为空或缺失，请使用以下内容创建它：

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. 让我们来理解这段 HTML 的作用：

   - 我们有一个标准的 HTML 文档结构，包含标题和视口设置
   - 我们链接到一个名为 `style.css` 的外部 CSS 文件
   - 我们包含一个标题和段落来解释我们的演示
   - 最重要的是，我们有一个带有 `zoom-in-out-box` 类的 `<div>` 元素，它将被用于动画

4. 如果你进行了任何更改，请保存 `index.html` 文件。

这个 div 元素将是我们创建动画的画布。在下一步中，我们将使用 CSS 对这个元素进行样式设置。
