# Enfants répartis régulièrement

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour répartir régulièrement les éléments enfants à l'intérieur d'un élément parent, utilisez la mise en page Flexbox en définissant la propriété `display` de l'élément parent sur `flex`. Pour répartir les enfants horizontalement avec un espace égal entre eux, utilisez `justify-content: space-between`. Pour répartir les enfants avec un espace autour d'eux, utilisez `justify-content: space-around`. Voici un exemple :

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
