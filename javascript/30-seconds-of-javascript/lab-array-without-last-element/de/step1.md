# Wie man ein Array ohne das letzte Element bekommt

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. So können Sie alle Elemente eines Arrays außer dem letzten zurückgeben:

- Verwenden Sie `Array.prototype.slice()`, um alle Elemente des Arrays außer dem letzten zurückzugeben.

```js
const initial = (arr) => arr.slice(0, -1);
```

Hier ist ein Beispiel:

```js
initial([1, 2, 3]); // [1, 2]
```
