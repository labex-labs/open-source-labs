# Drop Cap

> `index.html`과 `style.css`에 코드를 작성할 수 있습니다.

첫 번째 단락의 첫 글자를 나머지 텍스트보다 더 크게 만듭니다.

- `:first-child` 선택자를 사용하여 첫 번째 단락만 선택합니다.
- `::first-letter` 의사 요소 (pseudo-element) 를 사용하여 단락의 첫 번째 요소를 스타일링합니다.

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
