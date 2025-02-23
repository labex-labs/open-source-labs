# Changer l'affichage en fonction de l'état de visibilité actuel

jQuery peut également vous permettre de changer la visibilité d'un contenu en fonction de son état de visibilité actuel. `.toggle()` affichera le contenu actuellement caché et cachera le contenu actuellement visible. Vous pouvez passer les mêmes arguments à `.toggle()` que ceux que vous passez à n'importe laquelle des méthodes d'effets ci-dessus.

```js
// Basculer instantanément l'affichage de tous les paragraphes
$("p").toggle();

// Basculer l'affichage de tous les divs en 1,8 secondes
$("div").toggle(1800);
```

`.toggle()` utilisera une combinaison d'effets de glissement et de fondu, tout comme `.show()` et `.hide()`.

> Vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
