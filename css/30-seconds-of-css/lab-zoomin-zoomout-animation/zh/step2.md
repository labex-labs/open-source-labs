# 基本 CSS 样式设置

既然我们已经有了 HTML 结构，接下来让我们为动画元素创建基本的 CSS 样式。

1. 在编辑器中打开 `style.css` 文件。

2. 如果文件为空或缺失，请使用以下内容创建它：

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. 让我们来理解这段 CSS 的作用：

   - 我们为页面设置了一些基本样式（字体、宽度和边距）
   - 我们将标题设置为深灰色
   - 对于我们的动画元素 `.zoom-in-out-box`，我们：
     - 在其周围添加了 24px 的边距
     - 将其宽度和高度设置为 50px
     - 为其赋予了鲜艳的粉色背景颜色

4. 完成这些更改后，保存 `style.css` 文件。

5. 要查看你的进度，请点击 VSCode 右下角的“Go Live”按钮。这将在端口 8080 上启动一个 Web 服务器。然后刷新 **Web 8080** 标签页，查看你设置好样式的盒子。

现在你应该在网页上看到一个小的粉色方块。这个方块就是我们将在接下来的步骤中进行动画处理的元素。
