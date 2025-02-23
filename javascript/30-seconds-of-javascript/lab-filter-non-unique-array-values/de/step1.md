# Wie man in JavaScript nicht eindeutige Werte aus einem Array herausfiltert

Um in JavaScript nicht eindeutige Werte aus einem Array herauszufiltern, kann man ein neues Array erstellen, das nur aus den eindeutigen Werten besteht. Hier ist, wie man es macht:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den `Set`-Konstruktor und den Spread-Operator (`...`), um ein Array der eindeutigen Werte im ursprünglichen Array zu erstellen.
3. Verwenden Sie `Array.prototype.filter()`, um ein Array zu erstellen, das nur aus den eindeutigen Werten besteht.

Hier ist eine Beispiel-Funktion, die dies tut:

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

Sie können diese Funktion mit jedem Array verwenden, um die nicht eindeutigen Werte herauszufiltern. Beispielsweise:

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
