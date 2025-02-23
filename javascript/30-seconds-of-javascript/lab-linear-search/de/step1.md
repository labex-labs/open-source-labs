# Lineare Suchalgorithmus

Um das Programmieren zu üben, öffnen Sie das Terminal oder SSH und geben Sie `node` ein. Der lineare Suchalgorithmus findet den ersten Index eines angegebenen Elements in einem Array.

So funktioniert es:

- Verwenden Sie eine `for...in`-Schleife, um über die Indizes des angegebenen Arrays zu iterieren.
- Überprüfen Sie, ob das Element am entsprechenden Index gleich `item` ist.
- Wenn das Element gefunden wird, geben Sie den Index zurück. Verwenden Sie den unären `+`-Operator, um es von einer Zeichenkette in eine Zahl umzuwandeln.
- Wenn das Element nicht gefunden wird, nachdem das gesamte Array durchlaufen wurde, geben Sie `-1` zurück.

Hier ist der Code:

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

Um die Funktion zu testen, rufen Sie sie mit einem Array und einem Wert zum Suchen auf:

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
