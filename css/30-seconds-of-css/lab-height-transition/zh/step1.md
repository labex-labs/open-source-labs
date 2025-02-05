# 高度过渡

虚拟机中已经提供了 `index.html` 和 `style.css`。

以下代码片段通过执行以下步骤，在元素高度未知时将其高度从 `0` 过渡到 `auto`：

- 使用 `transition` 属性指定对 `max-height` 的更改应在 `0.3 秒` 的持续时间内进行过渡。
- 将 `overflow` 属性设置为 `hidden`，以防止隐藏元素的内容溢出其容器。
- 使用 `max-height` 属性指定初始高度为 `0`。
- 使用 `:hover` 伪类将 `max-height` 更改为由 JavaScript 设置的 `--max-height` 变量的值。
- 使用 `Element.scrollHeight` 属性和 `CSSStyleDeclaration.setProperty()` 方法将 `--max-height` 的值设置为元素的当前高度。
- **注意**：此方法会在每个动画帧上导致重排，当过渡元素下方有大量元素时，可能会导致延迟。

```html
<div class="trigger">
  悬停在我上面以查看高度过渡。
  <div class="el">附加内容</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页以预览网页。
