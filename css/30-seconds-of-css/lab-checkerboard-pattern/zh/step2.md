# 创建 HTML 结构

既然我们已经了解了项目文件，接下来让我们为棋盘图案创建 HTML 结构。

1. 再次在编辑器中打开 `index.html` 文件。

2. 我们需要为棋盘图案添加一个容器元素。在 `<body>` 标签内，将注释替换为一个类名为 "checkerboard" 的 `<div>` 元素：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. 按下 Ctrl+S 组合键或点击“文件” > “保存”来保存 `index.html` 文件。

4. 现在，让我们添加一些基本的 CSS 来定义棋盘的尺寸。打开 `style.css` 文件并添加以下代码：

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

这段 CSS 代码的作用如下：

- 将棋盘的宽度和高度设置为 240 像素
- 将背景颜色设置为白色 (#fff)

5. 保存 `style.css` 文件。

6. 刷新 **Web 8080** 标签页以查看更改。

此时你应该会看到一个宽高均为 240 像素的白色方块。这将是我们绘制棋盘图案的画布。
