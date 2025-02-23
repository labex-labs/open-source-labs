# Configuration de plusieurs réponses aux événements

Très souvent, les éléments de votre application seront liés à plusieurs événements. Si plusieurs événements doivent partager la même fonction de gestion, vous pouvez fournir les types d'événements sous forme d'une liste séparée par des espaces à `.on()` :

```js
// Plusieurs événements, même gestionnaire
$("div").on(
  "click change", // Liez des gestionnaires pour plusieurs événements
  function () {
    console.log("Un élément de formulaire a été cliqué ou modifié!");
  }
);
```

Lorsque chaque événement a son propre gestionnaire, vous pouvez passer un objet à `.on()` avec une ou plusieurs paires clé/valeur, la clé étant le nom de l'événement et la valeur étant la fonction pour gérer l'événement.

```js
// Liaison de plusieurs événements avec différents gestionnaires
$("div").on({
  click: function () {
    console.log("cliqué!");
  },
  mouseover: function () {
    console.log("survolé!");
  }
});
```

> Vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
