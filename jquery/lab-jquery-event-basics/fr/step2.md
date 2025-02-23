# Étendre les événements à de nouveaux éléments de page

Il est important de noter que `.on()` ne peut créer des écouteurs d'événements que sur les éléments qui existent au moment où vous configurez les écouteurs. Par exemple :

```js
$(document).ready(function () {
  // Maintenant, créez un nouveau bouton avec la classe alert.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Configure le comportement de clic sur tous les éléments de bouton avec la classe alert
  // qui existent dans le DOM lorsque l'instruction est exécutée
  $("button.alert").on("click", function () {
    console.log("Un bouton avec la classe alert a été cliqué!");
  });
});
```

Si des éléments similaires sont créés après la configuration des écouteurs d'événements, ils ne prendront pas automatiquement les comportements d'événement que vous avez configurés précédemment.

> Vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
