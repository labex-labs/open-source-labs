# Primzahlen mit dem Sieb des Eratosthenes generieren

Um Primzahlen bis zu einer angegebenen Zahl mit dem Sieb des Eratosthenes zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Erstellen Sie ein Array, das alle Zahlen von `2` bis zur angegebenen Zahl enthält.
3. Verwenden Sie `Array.prototype.filter()`, um die Werte zu filtern, die durch jede Zahl von `2` bis zur Quadratwurzel der angegebenen Zahl teilbar sind.
4. Geben Sie das resultierende Array mit Primzahlen zurück.

Hier ist der JavaScript-Code, um Primzahlen bis zu einer angegebenen Zahl zu generieren:

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

Sie können die Funktion `generatePrimes()` aufrufen, indem Sie die gewünschte Zahl als Argument übergeben. Beispiel:

```js
generatePrimes(10); // [2, 3, 5, 7]
```
