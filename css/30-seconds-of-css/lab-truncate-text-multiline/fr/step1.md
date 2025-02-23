# Tronquer un texte multiligne

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour tronquer un texte qui est plus long qu'une ligne, suivez ces étapes :

1. Utilisez `overflow: hidden` pour empêcher le texte de déborder de ses dimensions.
2. Fixez une largeur (`width`) de `400px` pour vous assurer que l'élément a au moins une dimension constante.
3. Fixez la hauteur (`height`) à `109,2px` en utilisant la formule `taille de police * hauteur de ligne * nombre de lignes` (dans ce cas `26 * 1,4 * 3 = 109,2`).
4. Ajoutez la classe `truncate-text-multiline` à l'élément `p` de votre HTML.
5. Fixez la taille de police (`font-size`) à `26px` et la hauteur de ligne (`line-height`) à `1,4` dans la feuille de style CSS pour la classe `.truncate-text-multiline`.
6. Fixez la couleur (`color`) à `#333` et le fond (`background`) à `#f5f6f9` pour styliser le texte.
7. Pour créer un gradient allant de `transparent` à la couleur de fond, ajoutez les règles CSS suivantes à l'élément pseudo-élément `.truncate-text-multiline::after` :

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36, 4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

Cela créera un conteneur de gradient avec une hauteur de `36,4px`, calculée pour le conteneur de gradient, en utilisant la formule `taille de police * hauteur de ligne` (dans ce cas `26 * 1,4 = 36,4`). L'élément pseudo-élément `::after` est positionné dans le coin inférieur droit de l'élément `.truncate-text-multiline`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
