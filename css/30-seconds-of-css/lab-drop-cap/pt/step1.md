# Drop Cap

> Você pode escrever o código em `index.html` e `style.css`.

Torna a primeira letra do primeiro parágrafo maior que o restante do texto.

- Use o seletor `:first-child` para selecionar apenas o primeiro parágrafo.
- Use o pseudo-elemento `::first-letter` para estilizar o primeiro elemento do parágrafo.

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
