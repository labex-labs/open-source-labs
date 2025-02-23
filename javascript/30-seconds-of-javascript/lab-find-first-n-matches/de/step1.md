# Wie man die ersten N Übereinstimmungen findet

Um die ersten `n` Elemente zu finden, die einem bestimmten Kriterium entsprechen, verwenden Sie die `findFirstN`-Funktion. Hier ist, wie:

1. Öffnen Sie das Terminal/SSH.
2. Tippen Sie `node`, um mit der Codeausführung zu beginnen.
3. Verwenden Sie die `findFirstN`-Funktion und übergeben Sie das Array, in dem Sie suchen möchten, eine Übereinstimmungsmethode und die Anzahl der Übereinstimmungen, die Sie finden möchten (wenn nicht angegeben, ist der Standardwert 1).
4. Die `matcher`-Funktion wird für jedes Element des `arr` ausgeführt, und wenn sie einen wahren Wert zurückgibt, wird dieses Element der Ergebnismenge hinzugefügt.
5. Wenn die Länge des `res`-Arrays `n` erreicht, gibt die Funktion das Ergebnismenge zurück.
6. Wenn keine Übereinstimmungen gefunden werden, wird ein leeres Array zurückgegeben.

Hier ist der Code für die `findFirstN`-Funktion:

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Und hier sind einige Beispiele für die Verwendung:

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
