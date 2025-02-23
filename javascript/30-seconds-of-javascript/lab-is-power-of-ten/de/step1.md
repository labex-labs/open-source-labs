# Überprüfen, ob eine Zahl eine Potenz von Zehn ist

Um zu überprüfen, ob eine Zahl eine Potenz von Zehn ist, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist der Code, den Sie verwenden können, um zu bestimmen, ob `n` eine Potenz von `10` ist:

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Verwenden Sie die `isPowerOfTen()`-Funktion, um zu bestimmen, ob eine gegebene Zahl eine Potenz von Zehn ist.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
