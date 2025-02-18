# Barre de progression de défilement (Scroll Progress Bar)

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour créer une barre de progression qui affiche le pourcentage de défilement d'une page web, suivez ces étapes :

1. Ajoutez un élément `div` avec l'`id` "scroll-progress" au code HTML.
2. Dans le code CSS, définissez la propriété `position` de l'élément sur `fixed`, la propriété `top` sur `0`, la propriété `width` sur `0%`, la propriété `height` sur `4px` et la couleur de fond (`background`) sur `#7983ff`.
3. Définissez la valeur de `z-index` sur un grand nombre pour vous assurer que la barre de progression est placée en haut de la page et au-dessus de tout contenu.
4. Dans le code JavaScript, sélectionnez l'élément `scroll-progress` en utilisant la méthode `document.getElementById()`.
5. Calculez la hauteur de la page web en utilisant la formule `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6. Ajoutez un écouteur d'événement à l'objet `window` qui écoute l'événement `scroll`.
7. Dans la fonction de l'écouteur d'événement, calculez le pourcentage de défilement du document en utilisant la formule `(scrollTop / height) * 100`.
8. Définissez la largeur (`width`) de l'élément `scroll-progress` sur le pourcentage de défilement en utilisant la propriété `style`.

Voici le code :

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

Cliquez sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
