# Secousse sur entrée invalide

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de secousse lorsqu'il y a une entrée invalide, suivez ces étapes :

1. Utilisez l'attribut `pattern` pour définir une expression régulière qui spécifie l'entrée autorisée. Par exemple, utilisez `[A-Za-z]*` pour autoriser uniquement des lettres.
2. Définissez une animation de secousse à l'aide de `@keyframes`. Réglez la propriété `margin-left` pour déplacer l'entrée vers la gauche et la droite.
3. Utilisez la pseudo-classe `:invalid` pour appliquer l'animation de secousse à l'entrée.
4. Facultativement, ajoutez une ombre portée rouge à l'entrée pour indiquer l'erreur.

Voici un extrait de code d'exemple :

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
