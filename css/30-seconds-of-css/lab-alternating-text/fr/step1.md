# Alternating Text

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de texte alterné, suivez ces étapes :

1. Créez un élément `<span>` avec une classe de "alternant" et un `id` de "alternating - text" pour contenir le texte qui sera alterné :

```html
<p>
  J'aime coder en <span class="alternating" id="alternating - text"></span>.
</p>
```

2. Dans le CSS, définissez une animation appelée `alternating - text` qui fera disparaître l'élément `<span>` en définissant `display: none` :

```css
.alternating {
  animation - name: alternating - text;
  animation - duration: 3s;
  animation - iteration - count: infinite;
  animation - timing - function: ease;
}

@keyframes alternating - text {
  90% {
    display: none;
  }
}
```

3. En JavaScript, définissez un tableau des différents mots qui seront alternés et utilisez le premier mot pour initialiser le contenu de l'élément `<span>` :

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating - text");

let i = 0;
element.innerHTML = texts[0];
```

4. Utilisez `EventTarget.addEventListener()` pour définir un écouteur d'événements pour l'événement `'animationiteration'`. Cela exécutera le gestionnaire d'événements chaque fois qu'une itération de l'animation est terminée. Dans le gestionnaire d'événements, utilisez `Element.innerHTML` pour afficher l'élément suivant dans le tableau `texts` comme contenu de l'élément `<span>` :

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
