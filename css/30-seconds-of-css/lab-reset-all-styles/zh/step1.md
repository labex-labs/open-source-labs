# 重置所有样式

虚拟机中已提供了 `index.html` 和 `style.css`。

要将所有样式重置为其默认值，请使用 `all` 属性。此属性不会影响 `direction` 和 `unicode-bidi` 属性。以下是使用它的示例：

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
