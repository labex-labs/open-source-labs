# Überprüfen, ob ein Wert arrayähnlich ist

Um zu überprüfen, ob ein Wert arrayähnlich ist, führen Sie die folgenden Schritte aus:

1. Öffnen Sie die Konsole/SSH.
2. Geben Sie `node` ein.
3. Verwenden Sie den folgenden Code, um zu überprüfen, ob das bereitgestellte Argument iterierbar ist:

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. Die Funktion gibt `true` zurück, wenn das bereitgestellte Argument ein arrayähnliches Objekt ist, andernfalls `false`.
5. Beispiel:

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
