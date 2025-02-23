# Séparateur de forme

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un élément séparateur entre deux blocs différents à l'aide d'une forme SVG, suivez ces étapes :

1. Utilisez l'élément pseudo-élément `::after`.
2. Ajoutez la forme SVG (un triangle de 24x12) via une URI de données à l'aide de la propriété `background-image`. L'image d'arrière-plan se répétera par défaut et couvrira toute la zone de l'élément pseudo-élément.
3. Définissez la couleur souhaitée pour le séparateur en utilisant la propriété `background` de l'élément parent.

Utilisez le code HTML suivant :

```html
<div class="shape-separator"></div>
```

Et appliquez les règles CSS suivantes :

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
