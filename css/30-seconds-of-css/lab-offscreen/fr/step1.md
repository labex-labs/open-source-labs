# Hors de l'écran

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Cette technique cache complètement un élément dans le DOM tout en le rendant toujours accessible. Pour y arriver, vous pouvez suivre ces étapes :

- Supprimez toutes les bordures et le rembourrage et cachez le débordement de l'élément.
- Utilisez `clip` pour vous assurer qu'aucune partie de l'élément n'est affichée.
- Définissez la `height` et la `width` de l'élément sur `1px` et annulez-les en utilisant `margin: -1px`.
- Utilisez `position: absolute` pour empêcher l'élément de prendre de l'espace dans le DOM.
- Notez que cette technique est une meilleure alternative à `display: none` (non lisible par les lecteurs d'écran) et `visibility: hidden` (prend de l'espace physique dans le DOM) en termes d'accessibilité et d'amiabilité pour la mise en page.

Voici un exemple de la manière dont vous pouvez utiliser cette technique en HTML et CSS :

```html
<a class="button" href="https://google.com">
  Découvrez-en plus <span class="offscreen">sur les pantalons</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
