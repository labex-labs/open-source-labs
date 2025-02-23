# Prüfen auf gleiche Inhalte in Arrays

Um zu prüfen, ob zwei Arrays die gleichen Elemente enthalten, unabhängig von der Reihenfolge, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein.
2. Verwenden Sie eine `for...of`-Schleife über einen `Set`, der aus den Werten beider Arrays erstellt wurde.
3. Verwenden Sie `Array.prototype.filter()`, um die Anzahl der Vorkommen jedes einzelnen Wertes in beiden Arrays zu vergleichen.
4. Geben Sie `false` zurück, wenn die Zählungen für irgendein Element nicht übereinstimmen, andernfalls `true`.

Hier ist der Code dazu:

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

Um die Funktion zu testen, verwenden Sie folgenden Code:

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
