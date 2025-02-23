# Hamburger Button

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un menu hamburger qui passe à un bouton croix au survol, suivez ces étapes :

1. Utilisez un conteneur `div` `.hamburger-menu` qui contient les barres supérieure, inférieure et centrale.
2. Définissez le conteneur sur `display: flex` avec `flex-flow: column wrap`.
3. Ajoutez un espacement entre les barres en utilisant `justify-content: space-between`.
4. Utilisez `transform: rotate()` pour faire tourner les barres supérieure et inférieure de 45 degrés et `opacity: 0` pour faire disparaître la barre centrale au survol.
5. Utilisez `transform-origin: left` pour que les barres tournent autour du point gauche.

Voici le code HTML correspondant :

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

Et voici le code CSS :

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
