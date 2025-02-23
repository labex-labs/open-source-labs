# Effet de machine à écrire

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation d'effet de machine à écrire, suivez ces étapes :

1. Définissez deux animations, `typing` et `blink`. `typing` anime les caractères, et `blink` anime le curseur.
2. Utilisez le pseudo-élément `::after` pour ajouter le curseur à l'élément conteneur.
3. Utilisez JavaScript pour définir le texte pour l'élément interne et définir la variable `--characters`, qui contient le nombre de caractères. Cette variable est utilisée pour animer le texte.
4. Utilisez `white-space: nowrap` et `overflow: hidden` pour rendre le contenu invisible si nécessaire.

Voici le code HTML :

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

Et voici le code CSS :

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

Et enfin, voici le code JavaScript :

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
