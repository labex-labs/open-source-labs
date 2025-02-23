# Masquer les éléments vides

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour masquer les éléments sans contenu, utilisez la pseudo-classe `:empty`. Par exemple, si vous avez le code HTML suivant :

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

Vous pouvez utiliser le code CSS suivant pour masquer l'élément bouton sans contenu :

```css
p:empty {
  display: none;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
