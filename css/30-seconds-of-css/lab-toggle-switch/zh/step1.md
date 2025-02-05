# 切换开关

虚拟机中已经提供了 `index.html` 和 `style.css`。

以下是更简洁明了的内容版本：

要仅用 CSS 创建一个切换开关，请按以下步骤操作：

1. 使用 `for` 属性将 `<label>` 与复选框 `<input>` 元素关联起来。
2. 使用 `<label>` 的 `::after` 伪元素为开关创建一个圆形旋钮。
3. 使用 `:checked` 伪类选择器，通过 `transform: translateX(20px)` 和开关的 `background-color` 来改变旋钮的位置。
4. 使用 `position: absolute` 和 `left: -9999px` 在视觉上隐藏 `<input>` 元素。

以下是 HTML 代码：

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

以下是 CSS 代码：

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
