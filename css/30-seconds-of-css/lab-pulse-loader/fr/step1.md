# Chargeur à effet d'impulsion

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de chargeur à effet d'impulsion à l'aide de la propriété `animation-delay`, suivez ces étapes :

1. Utilisez `@keyframes` pour définir une animation pour deux éléments `<div>`. Définissez le point de départ (`0%`) pour les deux éléments pour qu'ils n'aient pas de `largeur` ou `hauteur` et soient positionnés au centre. Pour le point de fin (`100%`), faites en sorte que les deux éléments augmentent en `largeur` et `hauteur`, mais remettent leur `position` à `0`.
2. Utilisez `opacity` pour effectuer une transition de `1` à `0` lors de l'animation pour donner aux éléments `<div>` un effet de disparition au fur et à mesure qu'ils s'étendent.
3. Définissez une `largeur` et une `hauteur` prédéfinies pour le conteneur parent, `.ripple-loader`. Utilisez `position: relative` pour positionner ses enfants.
4. Utilisez `animation-delay` sur le deuxième élément `<div>`, de sorte que chaque élément démarre son animation à un moment différent.

Voici le code HTML et CSS pour y arriver :

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
