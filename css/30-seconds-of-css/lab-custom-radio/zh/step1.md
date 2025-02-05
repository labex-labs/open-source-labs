# 自定义单选按钮

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个在状态变化时带有动画效果的样式化单选按钮，请按照以下步骤操作：

1. 使用弹性盒模型（Flexbox）创建一个 `.radio-container`，为单选按钮创建合适的布局。
2. 重置 `<input>` 元素的样式，并用它来创建单选按钮的轮廓和背景。
3. 使用 `::before` 元素创建单选按钮的内圈。
4. 通过使用 `transform: scale(1)` 和 CSS 过渡，在状态变化时创建动画效果。

以下是一个 HTML 代码片段示例：

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">苹果</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">橙子</label>
</div>
```

以及相应的 CSS：

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

请点击右下角的“Go Live”，在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
