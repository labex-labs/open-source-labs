# 修剪多行文本

> 你可以在 `index.html` 和 `style.css` 中编写代码。

将多行文本限制为给定的行数。

- 使用 `-webkit-line-clamp` 设置要显示的最大行数。
- 将 `display` 设置为 `-webkit-box`，并将 `-webkit-box-orient` 设置为 `vertical`，因为应用 `-webkit-line-clamp` 需要它们。
- 应用 `overflow: hidden` 以在文本修剪后隐藏任何溢出内容。

```html
<p class="excerpt">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod enim
  eget ultricies sollicitudin. Nunc aliquam arcu arcu, non suscipit metus luctus
  id. Aliquam sodales turpis ipsum, in vehicula dui tempor sit amet. Nullam quis
  urna erat. Pellentesque mattis dolor purus. Aliquam nisl urna, tempor a
  euismod a, placerat in mauris. Phasellus neque quam, dapibus quis nunc at,
  feugiat suscipit tortor. Duis vel posuere dolor. Phasellus risus erat,
  lobortis et mi vel, viverra faucibus lectus. Etiam ut posuere sapien. Nulla
  ultrices dui turpis, interdum consectetur urna tempus at.
</p>
```

```css
.excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```
