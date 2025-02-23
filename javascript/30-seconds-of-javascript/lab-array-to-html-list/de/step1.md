# Umwandeln eines Arrays in eine HTML-Liste

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion wandelt die gegebenen Array-Elemente in `<li>`-Tags um und fügt sie zur Liste mit der gegebenen ID hinzu.

Verwenden Sie `Array.prototype.map()` und `Document.querySelector()`, um eine Liste von HTML-Tags zu generieren.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Beispielverwendung:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
