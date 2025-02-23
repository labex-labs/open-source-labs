# Ombre dynamique

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une ombre basée sur les couleurs d'un élément, suivez ces étapes :

1. Utilisez le pseudo-élément `::after` avec `position: absolute` et `width` et `height` définis sur `100%` pour remplir l'espace disponible dans l'élément parent.

2. Héritez du `background` de l'élément parent en utilisant `background: inherit`.

3. Décalez légèrement le pseudo-élément en utilisant `top`. Ensuite, utilisez `filter: blur()` pour créer une ombre et définissez `opacity` pour la rendre semi-transparente.

4. Positionnez le pseudo-élément derrière son parent en définissant `z-index: -1`. Définissez `z-index: 1` sur l'élément parent.

Voici un exemple de code HTML et CSS :

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
