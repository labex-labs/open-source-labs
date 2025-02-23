# Liste à rayures zébrées

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une liste avec des couleurs d'arrière-plan alternées, utilisez les sélecteurs de pseudo-classes `:nth-child(odd)` ou `:nth-child(even)` pour appliquer une `background-color` différente aux éléments en fonction de leur position parmi les frères et sœurs. Cela peut être appliqué à divers éléments HTML tels que `<div>`, `<tr>`, `<p>`, `<ol>`, etc.

Voici un exemple de création d'une liste rayée avec des éléments `<li>` :

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
