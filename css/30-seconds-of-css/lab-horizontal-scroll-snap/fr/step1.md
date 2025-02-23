# Défilement horizontal avec prise en charge des points d'arrêt

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un conteneur horizontalement défilemable qui s'arrête sur des éléments lors du défilement, suivez ces étapes :

1. Utilisez `display: grid` et `grid-auto-flow: column` pour créer une disposition horizontale.
2. Utilisez `scroll-snap-type: x mandatory` et `overscroll-behavior-x: contain` pour créer un effet de prise en charge des points d'arrêt lors du défilement horizontal.
3. Changez `scroll-snap-align` en `start`, `stop` ou `center` pour ajuster l'alignement des points d'arrêt.

Voici un exemple de code HTML et CSS que vous pouvez utiliser :

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
