# Evénements

> Le fichier `index.html` a déjà été fourni dans la machine virtuelle.

Pour que les sites web soient réellement interactifs, il est nécessaire d'utiliser des gestionnaires d'événements. Ce sont des structures de code qui écoutent les activités dans le navigateur et exécutent du code en réponse. L'exemple le plus évident est la gestion de l'[événement click](https://developer.mozilla.org/fr/docs/Web/API/Element/click_event), qui est déclenché par le navigateur lorsque vous cliquez sur quelque chose avec la souris. Pour le démontrer, entrez le code suivant dans votre console, puis cliquez sur la page web actuelle :

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

Il existe plusieurs façons d'attacher un gestionnaire d'événements à un élément.
Ici, nous sélectionnons l'élément [`<html>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/html). Nous appelons ensuite sa fonction [`addEventListener()`](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener), en lui passant le nom de l'événement à écouter (`'click'`) et une fonction à exécuter lorsque l'événement se produit.

La fonction que nous venons de passer à `addEventListener()` ici est appelée une _fonction anonyme_, car elle n'a pas de nom. Il existe une autre façon d'écrire les fonctions anonymes, que nous appelons une _fonction fléchée_.
Une fonction fléchée utilise `() =>` au lieu de `function ()` :

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

> Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
