# 首字下沉

> 你可以在`index.html`和`style.css`中编写代码。

使第一段的首字母比文本的其余部分更大。

- 使用`:first-child`选择器仅选择第一段。
- 使用`::first-letter`伪元素为段落的第一个元素设置样式。

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
