# Überprüfen, ob ein Wert objektähnlich ist

Um zu überprüfen, ob ein Wert objektähnlich ist, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein, um mit der Codeausführung zu beginnen.
3. Überprüfen Sie, ob der bereitgestellte Wert nicht `null` ist und seine `typeof` gleich `'object'` ist.

Hier ist der Code, den Sie verwenden können:

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

Sie können diese Funktion mit den folgenden Beispielen testen:

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
