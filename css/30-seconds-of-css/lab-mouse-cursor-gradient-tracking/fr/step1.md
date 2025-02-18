# Suivi du gradient du curseur de la souris

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet de survol où le gradient suit le curseur de la souris, suivez ces étapes :

1. Déclarez deux variables CSS, `--x` et `--y`, pour suivre la position de la souris sur le bouton.
2. Déclarez une variable CSS, `--size`, pour modifier les dimensions du gradient.
3. Utilisez `background: radial-gradient(circle closest-side, pink, transparent)` pour créer le gradient à la bonne position.
4. Enregistrez un gestionnaire pour l'événement `'mousemove'` en utilisant `Document.querySelector()` et `EventTarget.addEventListener()`.
5. Mettez à jour les valeurs des variables CSS `--x` et `--y` en utilisant `Element.getBoundingClientRect()` et `CSSStyleDeclaration.setProperty()`.

Voici le code HTML pour le bouton :

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

Et voici le code CSS :

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Enfin, voici le code JavaScript :

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
