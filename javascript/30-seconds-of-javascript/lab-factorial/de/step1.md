# Die Fakultät einer Zahl berechnen

Um die Fakultät einer Zahl zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Rekursion, um die Fakultät zu berechnen.
3. Wenn `n` kleiner oder gleich `1` ist, geben Sie `1` zurück.
4. Andernfalls geben Sie das Produkt von `n` und der Fakultät von `n - 1` zurück.
5. Wenn `n` eine negative Zahl ist, werfen Sie einen `TypeError`.

Hier ist der Code, um die Fakultät zu berechnen:

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

Sie können den Code testen, indem Sie die `factorial`-Funktion mit einer Zahl als Argument aufrufen:

```js
factorial(6); // 720
```
