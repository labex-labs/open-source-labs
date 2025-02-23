# Wie man in JavaScript die ersten n Elemente eines Arrays erhält

Um die ersten `n` Elemente eines Arrays in JavaScript zu erhalten, kannst du die `Array.prototype.slice()`-Methode verwenden. Hier ist wie:

```js
const firstN = (arr, n) => arr.slice(0, n);
```

In diesem Codeausschnitt repräsentiert `arr` das Array, aus dem du die Elemente extrahieren möchtest, und `n` die Anzahl der Elemente, die du extrahieren möchtest. Die `slice()`-Methode nimmt zwei Argumente: den Startindex (der in diesem Fall `0` ist) und den Endindex (der `n` ist). Die Methode gibt ein neues Array zurück, das die extrahierten Elemente enthält.

Hier ist ein Beispiel, wie du die `firstN()`-Funktion verwendest:

```js
firstN(["a", "b", "c", "d"], 2); // ['a', 'b']
```

Dies wird die ersten beiden Elemente des `['a', 'b', 'c', 'd']`-Arrays zurückgeben, nämlich `['a', 'b']`.
