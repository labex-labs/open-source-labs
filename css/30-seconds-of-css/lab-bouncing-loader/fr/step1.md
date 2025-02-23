# Chargeur rebondissant

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de chargeur rebondissant :

1. Définissez une animation `@keyframes` qui utilise les propriétés `opacity` et `transform`, avec une translation sur un seul axe sur `transform: translate3d()` pour une meilleure performance.
2. Créez un conteneur parent avec la classe `.bouncing-loader` qui utilise `display: flex` et `justify-content: center` pour centrer les cercles rebondissants.
3. Donnez aux trois éléments `<div>` pour les cercles rebondissants la même `largeur`, `hauteur` et `border-radius: 50%` pour les rendre circulaires.
4. Appliquez l'animation `bouncing-loader` à chacun des trois cercles rebondissants.
5. Utilisez un `animation-delay` différent pour chaque cercle et `animation-direction: alternate` pour créer l'effet approprié.

Voici le code HTML :

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

Et voici le code CSS :

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
