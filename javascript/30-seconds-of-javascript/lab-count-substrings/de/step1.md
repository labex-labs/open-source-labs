# Wie man in JavaScript Teilzeichenfolgen in einer Zeichenfolge zählt

Wenn Sie sich in der Programmierung üben möchten, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese JavaScript-Funktion zählt die Anzahl der Vorkommen einer bestimmten Teilzeichenfolge in einer gegebenen Zeichenfolge.

Um diese Funktion zu verwenden, folgen Sie diesen Schritten:

1. Deklarieren Sie eine Funktion namens `countSubstrings`, die zwei Parameter annimmt: `str` und `searchValue`.
2. Initialisieren Sie zwei Variablen: `count` und `i`.
3. Verwenden Sie die `Array.prototype.indexOf()`-Methode, um `searchValue` in `str` zu suchen.
4. Wenn der Wert gefunden wird, erhöhen Sie die `count`-Variable und aktualisieren Sie die `i`-Variable.
5. Verwenden Sie eine `while`-Schleife, die sofort beendet wird, sobald der Wert, der von `Array.prototype.indexOf()` zurückgegeben wird, `-1` ist.
6. Geben Sie die `count`-Variable zurück.

Hier ist der Code für die `countSubstrings`-Funktion:

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

Sie können die Funktion mit den folgenden Beispielen testen:

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
