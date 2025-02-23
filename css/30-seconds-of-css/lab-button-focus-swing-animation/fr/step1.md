# Animation de balancier du bouton

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de balancier au survol, vous devriez utiliser une `transition` appropriée pour animer les changements de l'élément. Ensuite, appliquez la pseudo-classe `:focus` à l'élément et utilisez `animation` avec `transform` pour le faire basculer. Enfin, ajoutez `animation-iteration-count` pour jouer l'animation une seule fois. Voici un exemple de la manière de procéder en HTML et CSS :

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
