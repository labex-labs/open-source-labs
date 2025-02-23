# Quelque chose après que l'animation est terminée

Une erreur courante lors de la mise en œuvre d'effets jQuery est de supposer que l'exécution de la prochaine méthode dans votre chaîne attendra que l'animation soit terminée.

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

Il est important de comprendre que `.fadeIn()` ci-dessus ne lance que l'animation. Une fois lancée, l'animation est exécutée en modifiant rapidement les propriétés CSS dans une boucle `setInterval()` de JavaScript. Lorsque vous appelez `.fadeIn()`, elle lance la boucle d'animation puis renvoie l'objet jQuery, le passant à `.addClass()` qui ajoutera alors la classe de style `lookAtMe` tandis que la boucle d'animation vient juste de démarrer.

Pour différer une action jusqu'après que l'animation soit terminée, vous devez utiliser une fonction de rappel d'animation. Vous pouvez spécifier votre fonction de rappel d'animation comme deuxième argument passé à l'une des méthodes d'animation discutées ci-dessus. Pour le bout de code ci-dessus, nous pouvons implémenter un rappel comme suit :

```js
// Fade in all hidden paragraphs; then add a style class to them (correct with animation callback)
$("div.hidden").fadeIn(1500, function () {
  // this = DOM element which has just finished being animated
  $(this).addClass("lookAtMe");
});
```

Notez que vous pouvez utiliser le mot clé `this` pour vous référer à l'élément DOM animé. Notez également que le rappel sera appelé pour chaque élément de l'objet jQuery. Cela signifie que si votre sélecteur ne renvoie aucun élément, votre fonction de rappel d'animation ne sera jamais exécutée! Vous pouvez résoudre ce problème en testant si votre sélection a renvoyé des éléments ; sinon, vous pouvez simplement exécuter le rappel immédiatement.

```js
// Run a callback even if there were no elements to animate
var someElement = $("#nonexistent");

var cb = function () {
  console.log("done!");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> Vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
