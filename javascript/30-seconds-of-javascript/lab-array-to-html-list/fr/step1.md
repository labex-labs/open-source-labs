# Conversion d'un tableau en liste HTML

Pour commencer à coder, lancez le Terminal/SSH et entrez `node`.

Cette fonction convertit les éléments de tableau donnés en balises `<li>` et les ajoute à la liste avec l'ID donné.

Utilisez `Array.prototype.map()` et `Document.querySelector()` pour générer une liste d'éléments HTML.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Utilisation de l'exemple :

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
