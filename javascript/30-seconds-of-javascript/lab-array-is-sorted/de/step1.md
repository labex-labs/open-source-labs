# Codeübung: Überprüfen, ob ein Array sortiert ist

Um die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion, um zu überprüfen, ob ein numerisches Array sortiert ist:

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

Um sie zu verwenden, übergeben Sie einem Array von Zahlen `isSorted()`. Die Funktion gibt `1` zurück, wenn das Array aufsteigend sortiert ist, `-1`, wenn es absteigend sortiert ist, und `0`, wenn es nicht sortiert ist.

Hier sind einige Beispiele:

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
