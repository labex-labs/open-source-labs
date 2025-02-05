# 波形链接悬停效果

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在悬停链接时创建波形效果，你可以按照以下步骤操作：

1. 使用 `linear-gradient` 为链接创建重复背景。

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. 为链接创建 `:hover` 状态，其 `background-image` 为一个数据 URL，包含一个带有波形路径的 SVG 和一个动画。

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift.3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. 使用以下 HTML 代码将链接添加到页面。

```html
<p>
  The <a class="squiggle" href="#">magnificent octopus</a> swam along
  gracefully.
</p>
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
