# ドロップキャップ

> コードは `index.html` と `style.css` に記述できます。

最初の段落の最初の文字を他のテキストよりも大きくします。

- `:first-child` セレクターを使用して、最初の段落のみを選択します。
- `::first-letter` 疑似要素を使用して、段落の最初の要素にスタイルを適用します。

```html
<p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam commodo
  ligula quis tincidunt cursus. Integer consectetur tempor ex eget hendrerit.
  Cras facilisis sodales odio nec maximus. Pellentesque lacinia convallis
  libero, rhoncus tincidunt ante dictum at. Nullam facilisis lectus tellus, sit
  amet congue erat sodales commodo.
</p>
<p>
  Donec magna erat, imperdiet non odio sed, sodales tempus magna. Integer vitae
  orci lectus. Nullam consectetur orci at pellentesque efficitur.
</p>
```

```css
p:first-child::first-letter {
  color: #5f79ff;
  float: left;
  margin: 0 8px 0 4px;
  font-size: 3rem;
  font-weight: bold;
  line-height: 1;
}
```
