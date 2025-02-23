# Majuscule initiale

> Vous pouvez écrire le code dans `index.html` et `style.css`.

Rend la première lettre du premier paragraphe plus grande que le reste du texte.

- Utilisez le sélecteur `:first-child` pour sélectionner uniquement le premier paragraphe.
- Utilisez le pseudo-élément `::first-letter` pour styliser le premier élément du paragraphe.

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
