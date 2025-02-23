# Convertir una matriz en una lista HTML

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Esta función convierte los elementos de la matriz dada en etiquetas `<li>` y los agrega a la lista con el id dado.

Utiliza `Array.prototype.map()` y `Document.querySelector()` para generar una lista de etiquetas HTML.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Uso de ejemplo:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
