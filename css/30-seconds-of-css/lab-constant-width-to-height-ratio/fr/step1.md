# Rapport constant largeur/hauteur

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Ce fragment de code assure qu'un élément avec une `largeur` variable conservera une valeur `hauteur` proportionnelle. Pour y arriver, appliquez `padding-top` sur le pseudo-élément `::before`, rendant la `hauteur` de l'élément égale à un pourcentage de sa `largeur`. La proportion de `hauteur` à `largeur` peut être modifiée selon les besoins. Par exemple, un `padding-top` de `100%` créera un carré réactif avec un rapport 1:1. Pour utiliser ce code, ajoutez simplement le code HTML suivant :

```html
<div class="constant-width-to-height-ratio"></div>
```

Ensuite, ajoutez le code CSS suivant :

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
