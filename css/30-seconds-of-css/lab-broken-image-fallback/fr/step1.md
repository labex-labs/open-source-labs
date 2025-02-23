# Substitut pour les images qui échouent à charger

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Lorsque le chargement d'une image échoue, affichez un message d'erreur à l'utilisateur. Pour ce faire, appliquez des styles à l'élément `img` comme si c'était un conteneur de texte, en définissant son affichage sur `block` et sa largeur sur 100%. Utilisez les pseudo-éléments `::before` et `::after` pour afficher respectivement le message d'erreur et l'URL de l'image. Ces éléments ne seront affichés que si le chargement de l'image échoue.

Voici un extrait de code d'exemple :

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Désolé, cette image n'est pas disponible.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
