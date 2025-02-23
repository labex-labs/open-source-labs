# Disposition en maçonnerie

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une disposition en style maçonnerie, utilisez `.masonry-container` comme conteneur principal et ajoutez `.masonry-columns` comme conteneur interne dans lequel les éléments `.masonry-brick` seront placés. La disposition est composée de "briques" qui s'emboîtent les unes les autres, formant un parfait assemblage. La `largeur` pour une disposition verticale et la `hauteur` pour une disposition horizontale peuvent être fixées.

Pour vous assurer que la disposition s'affiche correctement, appliquez `display: block` aux éléments `.masonry-brick`. Utilisez le sélecteur de pseudo-élément `:first-child` pour appliquer une marge différente au premier élément pour tenir compte de sa positionnement.

Pour plus de flexibilité et de réactivité, utilisez des variables CSS et des requêtes média. Le `.masonry-container` a des variables CSS pour le nombre de colonnes et l'espacement. Le nombre de colonnes est contrôlé par des requêtes média qui spécifient différents nombres de colonnes et largeurs pour différentes tailles d'écran.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="Une image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Une autre image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Une autre image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="Une autre image de plus"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="Et une autre encore"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="La dernière"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
