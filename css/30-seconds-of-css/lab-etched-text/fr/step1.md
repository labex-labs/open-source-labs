# Texte gravé

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet de texte "gravé" ou incrusté sur un fond, utilisez les propriétés CSS suivantes :

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

La propriété `text-shadow` crée une ombre blanche décalée de `0px` horizontalement et de `2px` verticalement par rapport à la position d'origine. Assurez-vous que le fond est plus foncé que l'ombre pour que l'effet fonctionne. De plus, la couleur du texte devrait être légèrement ternie pour donner l'impression qu'elle a été taillée dans le fond. Enfin, appliquez la classe `etched-text` à l'élément HTML souhaité, tel qu'un paragraphe, pour obtenir l'effet.

```html
<p class="etched-text">I appear etched into the background.</p>
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
