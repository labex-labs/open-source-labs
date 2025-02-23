# Typographie fluide

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un texte qui s'adapte en taille en fonction de la largeur de la fenêtre d'affichage, vous pouvez utiliser CSS. Une façon de le faire est d'utiliser la fonction `clamp()` pour définir les tailles de police minimale et maximale. Une autre façon est d'utiliser une formule pour calculer une valeur réactive pour la taille de police. Voici un exemple d'élément HTML avec une classe `fluid-type` :

```html
<p class="fluid-type">Hello World!</p>
```

Voici le code CSS correspondant qui définit la taille de police pour qu'elle s'adapte entre `1rem` et `3rem` en fonction de la largeur de la fenêtre d'affichage :

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
