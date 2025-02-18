# Animation de zoom avant - zoom arrière

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour créer une animation de zoom avant - zoom arrière, suivez ces étapes :

1. Définissez une animation en trois étapes en utilisant `@keyframes`. À `0%` et `100%`, définissez l'élément à sa taille d'origine en utilisant `scale(1,1)`. À `50%`, agrandissez - le à 1,5 fois sa taille d'origine en utilisant `scale(1.5,1.5)`.

2. Donnez à l'élément une taille spécifique en utilisant `width` et `height`.

3. Utilisez `animation` pour définir les valeurs appropriées pour l'élément afin de le rendre animé.

Voici un exemple de code HTML et CSS :

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

Cliquez sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
