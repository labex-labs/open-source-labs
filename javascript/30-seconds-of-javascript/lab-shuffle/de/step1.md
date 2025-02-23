# Array-Misch-Algorithmus

Um ein Array in JavaScript zu mischen, verwenden Sie den Fisher-Yates-Algorithmus. Dieser Algorithmus ordnet die Elemente des Arrays zufällig neu an und gibt ein neues Array zurück.

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist der Code für den Fisher-Yates-Algorithmus:

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

Um ein Array zu mischen, übergeben Sie das Array an die `shuffle`-Funktion und sie wird das gemischte Array zurückgeben. Beispiel:

```js
const foo = [1, 2, 3];
shuffle(foo); // gibt [2, 3, 1] zurück, und foo ist immer noch [1, 2, 3]
```
