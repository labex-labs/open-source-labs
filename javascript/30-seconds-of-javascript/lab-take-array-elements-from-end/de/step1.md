# Wie man in JavaScript Arrayelemente vom Ende entfernt

Um in JavaScript Elemente vom Ende eines Arrays zu entfernen, kannst du die `Array.prototype.slice()`-Methode verwenden. Hier ist, wie du es tun kannst:

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

Diese Funktion erstellt ein neues Array mit den letzten `n` Elementen des ursprünglichen Arrays. Hier ist, wie du sie verwenden kannst:

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

Um diese Funktion zu verwenden, öffne das Terminal/SSH und tippe `node`, um zu beginnen, zu programmieren.
