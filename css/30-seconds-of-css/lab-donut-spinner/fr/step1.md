# Donut Spinner

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour indiquer le chargement du contenu, créez un donut spinner avec une `bordure` semi-transparente pour tout l'élément. Excluez un côté pour servir d'indicateur de chargement du donut. Ensuite, définissez et utilisez une animation appropriée, en utilisant `transform: rotate()` pour faire tourner l'élément. Voici un exemple de code en HTML et CSS :

HTML :

```html
<div class="donut"></div>
```

CSS :

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
