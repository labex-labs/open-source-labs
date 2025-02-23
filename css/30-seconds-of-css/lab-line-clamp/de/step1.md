# Mehrzeiligen Text kürzen

> Sie können den Code in `index.html` und `style.css` schreiben..

Mehrzeiligen Text auf eine gegebene Anzahl von Zeilen begrenzen.

- Verwenden Sie `-webkit-line-clamp`, um die maximale Anzahl der anzuzeigenden Zeilen festzulegen.
- Setzen Sie `display` auf `-webkit-box` und `-webkit-box-orient` auf `vertikal`, da diese erforderlich sind, damit `-webkit-line-clamp` angewendet werden kann.
- Wenden Sie `overflow: hidden` an, um alles, was nach dem Kürzen des Texts überläuft, zu verstecken.

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
