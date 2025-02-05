# 自定义复选框

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个在状态更改时带有动画效果的样式化复选框：

1. 创建一个作为 `<svg>` 元素的选中符号，并在其中包含一个 `<symbol>` 元素。使用 `<use>` 元素将其作为可重复使用的 SVG 图标插入。
2. 创建一个类名为 `.checkbox-container` 的容器 div。使用弹性盒模型（Flexbox）为复选框创建合适的布局。
3. 隐藏 `<input>` 元素，并将一个标签与其关联，以显示复选框和提供的文本。
4. 要在状态更改时为选中符号设置动画，使用 `stroke-dashoffset`。
5. 要创建缩放动画效果，通过 CSS 动画使用 `transform: scale(0.9)`。

HTML：

```html
<svg class="checkbox-symbol">
  <symbol id="check" viewbox="0 0 12 10">
    <polyline
      points="1.5 6 4.5 9 10.5 1"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
    ></polyline>
  </symbol>
</svg>

<div class="checkbox-container">
  <input class="checkbox-input" id="apples" type="checkbox" />
  <label class="checkbox" for="apples">
    <span>
      <svg width="12px" height="10px">
        <use xlink:href="#check"></use>
      </svg>
    </span>
    <span>苹果</span>
  </label>
  <input class="checkbox-input" id="oranges" type="checkbox" />
  <label class="checkbox" for="oranges">
    <span>
      <svg width="12px" height="10px">
        <use xlink:href="#check"></use>
      </svg>
    </span>
    <span>橙子</span>
  </label>
</div>
```

CSS：

```css
.checkbox-symbol {
  position: absolute;
  width: 0;
  height: 0;
  pointer-events: none;
  user-select: none;
}

.checkbox-container {
  box-sizing: border-box;
  background: #ffffff;
  color: #222;
  height: 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: row wrap;
}

.checkbox-container * {
  box-sizing: border-box;
}

.checkbox-input {
  position: absolute;
  visibility: hidden;
}

.checkbox {
  user-select: none;
  cursor: pointer;
  padding: 6px 8px;
  border-radius: 6px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
}

.checkbox:not(:last-child) {
  margin-right: 6px;
}

.checkbox:hover {
  background: rgba(0, 119, 255, 0.06);
}

.checkbox span {
  vertical-align: middle;
  transform: translate3d(0, 0, 0);
}

.checkbox span:first-child {
  position: relative;
  flex: 0 0 18px;
  width: 18px;
  height: 18px;
  border-radius: 4px;
  transform: scale(1);
  border: 1px solid #cccfdb;
  transition: all 0.3s ease;
}

.checkbox span:first-child svg {
  position: absolute;
  top: 3px;
  left: 2px;
  fill: none;
  stroke: #fff;
  stroke-dasharray: 16px;
  stroke-dashoffset: 16px;
  transition: all 0.3s ease;
  transform: translate3d(0, 0, 0);
}

.checkbox span:last-child {
  padding-left: 8px;
  line-height: 18px;
}

.checkbox:hover span:first-child {
  border-color: #0077ff;
}

.checkbox-input:checked + .checkbox span:first-child {
  background: #0077ff;
  border-color: #0077ff;
  animation: zoom-in-out 0.3s ease;
}

.checkbox-input:checked + .checkbox span:first-child svg {
  stroke-dashoffset: 0;
}

@keyframes zoom-in-out {
  50% {
    transform: scale(0.9);
  }
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
