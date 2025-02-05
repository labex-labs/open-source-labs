# 鼠标光标渐变跟踪

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建渐变跟随鼠标光标的悬停效果，请执行以下步骤：

1. 声明两个 CSS 变量 `--x` 和 `--y`，用于跟踪鼠标在按钮上的位置。
2. 声明一个 CSS 变量 `--size`，用于修改渐变的尺寸。
3. 使用 `background: radial-gradient(circle closest-side, pink, transparent)` 在正确的位置创建渐变。
4. 使用 `Document.querySelector()` 和 `EventTarget.addEventListener()` 注册 `'mousemove'` 事件的处理程序。
5. 使用 `Element.getBoundingClientRect()` 和 `CSSStyleDeclaration.setProperty()` 更新 `--x` 和 `--y` CSS 变量的值。

以下是按钮的 HTML 代码：

```html
<button class="mouse-cursor-gradient-tracking">
  <span>悬停在我上面</span>
</button>
```

以下是 CSS 代码：

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

最后，以下是 JavaScript 代码：

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
