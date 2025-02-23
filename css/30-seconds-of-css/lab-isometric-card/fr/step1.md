# Carte isométrique

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une carte isométrique, utilisez `transform` avec `rotateX()` et `rotateZ()` ainsi qu'un `box-shadow`. Vous pouvez également ajouter une `transition` pour animer la carte et créer un effet de levage lorsque l'utilisateur survole la carte.

Voici un extrait de code d'exemple :

```html
<div class="isometric-card"></div>
```

```css
.isometric-card {
  margin: 0 auto;
  transform: rotateX(51deg) rotateZ(43deg);
  transform-style: preserve-3d;
  background-color: #fcfcfc;
  will-change: transform;
  width: 240px;
  height: 320px;
  border-radius: 2rem;
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    28px 28px 28px 0 rgba(34, 33, 81, 0.25);
  transition:
    transform 0.4s ease-in-out,
    box-shadow 0.3s ease-in-out;
}

.isometric-card:hover {
  transform: translate3d(0px, -16px, 0px) rotateX(51deg) rotateZ(43deg);
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    54px 54px 28px -10px rgba(34, 33, 81, 0.15);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
