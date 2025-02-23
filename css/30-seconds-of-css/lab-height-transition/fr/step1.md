# Transition de hauteur

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Ce fragment de code effectue une transition de la hauteur d'un élément de `0` à `auto` lorsque sa hauteur est inconnue en effectuant les étapes suivantes :

- Utilisez la propriété `transition` pour spécifier que les modifications de `max-height` doivent être animées sur une durée de `0,3 s`.
- Utilisez la propriété `overflow` définie sur `hidden` pour empêcher le contenu de l'élément caché de déborder de son conteneur.
- Utilisez la propriété `max-height` pour spécifier une hauteur initiale de `0`.
- Utilisez le pseudo-classe `:hover` pour changer la `max-height` à la valeur de la variable `--max-height` définie par JavaScript.
- Utilisez la propriété `Element.scrollHeight` et la méthode `CSSStyleDeclaration.setProperty()` pour définir la valeur de `--max-height` à la hauteur actuelle de l'élément.
- **Remarque** : Cette approche provoque un reflow à chaque trame d'animation, ce qui peut entraîner un ralentissement lorsqu'il y a un grand nombre d'éléments en dessous de l'élément en transition.

```html
<div class="trigger">
  Survolez-moi pour voir une transition de hauteur.
  <div class="el">Contenu supplémentaire</div>
</div>
```

```css
.el {
  transition:
    max-height 0,
    3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
