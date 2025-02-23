# Configuration des réponses aux événements sur les éléments DOM

> `index.html` a déjà été fourni dans la machine virtuelle.

jQuery facilite la configuration de réponses basées sur des événements pour les éléments de la page. Ces événements sont souvent déclenchés par l'interaction de l'utilisateur final avec la page, par exemple lorsqu'un texte est entré dans un élément de formulaire ou que le pointeur de la souris est déplacé. Dans certains cas, tels que les événements de chargement et de déchargement de la page, le navigateur lui-même déclenchera l'événement.

jQuery propose des méthodes pratiques pour la plupart des événements natifs du navigateur. Ces méthodes - y compris `.click()`, `.focus()`, `.blur()`, `.change()`, etc. - sont des raccourcis pour la méthode `.on()` de jQuery. La méthode `on` est utile pour lier la même fonction de gestionnaire à plusieurs événements, lorsque vous voulez fournir des données au gestionnaire d'événements, lorsque vous travaillez avec des événements personnalisés ou lorsque vous voulez passer un objet de plusieurs événements et gestionnaires.

```js
// Configuration de l'événement en utilisant une méthode pratique
$("p").click(function () {
  console.log("Vous avez cliqué sur un paragraphe!");
});
```

```js
// Configuration de l'événement équivalente en utilisant la méthode `.on()`
$("p").on("click", function () {
  console.log("click");
});
```

> Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
