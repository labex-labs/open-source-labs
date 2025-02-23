# Raccourcir un texte multiligne

> Vous pouvez écrire le code dans `index.html` et `style.css`..

Limitez un texte multiligne à un nombre donné de lignes.

- Utilisez `-webkit-line-clamp` pour définir le nombre maximum de lignes à afficher.
- Définissez `display` sur `-webkit-box` et `-webkit-box-orient` sur `vertical`, car ils sont requis pour appliquer `-webkit-line-clamp`.
- Appliquez `overflow: hidden` pour masquer tout dépassement après que le texte ait été raccourci.

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
