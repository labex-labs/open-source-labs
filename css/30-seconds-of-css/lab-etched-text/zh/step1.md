# 蚀刻文本

虚拟机中已提供了 `index.html` 和 `style.css`。

要为背景上的文本创建“蚀刻”或雕刻效果，请使用以下 CSS 属性：

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

`text-shadow` 属性会创建一个白色阴影，从原点位置水平偏移 `0px`，垂直偏移 `2px`。要使效果生效，请确保背景比阴影暗。此外，文本颜色应稍微淡化，使其看起来像是从背景中雕刻出来的。最后，将 `etched-text` 类应用于所需的 HTML 元素，例如段落，以实现该效果。

```html
<p class="etched-text">I appear etched into the background.</p>
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
