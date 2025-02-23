# Dégradé de défilement d'éléments débordants

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour ajouter un dégradé poussant à un élément débordant et indiquer qu'il y a plus de contenu à défiler, suivez ces étapes :

1. Utilisez le pseudo-élément `::after` pour créer un `linear-gradient()` qui passe du `transparent` au `blanc` (du haut en bas).
2. Positionnez et dimensionnez le pseudo-élément dans son parent à l'aide de `position: absolute`, `width` et `height`.
3. Excluez le pseudo-élément des événements de souris en utilisant `pointer-events: none`, permettant ainsi le texte derrière lui d'être toujours sélectionnable/interactif.

Voici un extrait de code HTML et CSS exemple :

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
