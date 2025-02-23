# Rapport de forme

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Ce code crée un conteneur réactif avec un rapport de forme spécifique à l'aide de propriétés personnalisées CSS et de la fonction `calc()`. Suivez ces étapes pour y arriver :

1. Définissez le rapport de forme souhaité à l'aide d'une propriété personnalisée CSS, `--aspect-ratio`.
2. Définissez la propriété `position` de l'élément conteneur sur `relative` et sa propriété `height` sur `0`.
3. Calculez la hauteur de l'élément conteneur à l'aide de la fonction `calc()` et de la propriété personnalisée `--aspect-ratio`, et définissez-la comme propriété `padding-bottom`.
4. Définissez l'enfant direct de l'élément conteneur sur `position: absolute`, `top: 0`, `left: 0`, `width: 100%` et `height: 100%`.
5. Maintenez le rapport de forme de l'élément enfant en définissant sa propriété `object-fit` sur `cover`.

Utilisez le code HTML et CSS suivant pour créer le conteneur :

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
