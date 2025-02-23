# 複数行のテキストをトリミングする

> コードは `index.html` と `style.css` に記述できます。

与えられた行数に複数行のテキストを制限します。

- `-webkit-line-clamp` を使用して表示する最大行数を設定します。
- `-webkit-line-clamp` を適用するために必要な `display` を `-webkit-box` に、`-webkit-box-orient` を `vertical` に設定します。
- テキストがトリミングされた後のオーバーフローを非表示にするために `overflow: hidden` を適用します。

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
