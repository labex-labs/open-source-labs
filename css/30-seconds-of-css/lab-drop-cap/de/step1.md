# Drop Cap

> Sie können den Code in `index.html` und `style.css` schreiben.

Lässt den ersten Buchstaben des ersten Absatzes größer erscheinen als der Rest des Textes.

- Verwenden Sie den `:first-child`-Selector, um nur den ersten Absatz auszuwählen.
- Verwenden Sie das `::first-letter`-Pseudo-Element, um das erste Element des Absatzes zu gestalten.

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
