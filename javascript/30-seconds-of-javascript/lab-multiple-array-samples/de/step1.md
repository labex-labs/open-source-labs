# Code-Praxis: Zufällige Elemente aus einem Array abrufen

Um die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Der folgende Code nutzt den Fisher-Yates-Algorithmus, um ein Array zu durchmischen und `n` zufällige, eindeutige Elemente an eindeutigen Schlüsseln aus dem Array abzurufen, bis zur Größe des Arrays.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

Um diesen Code zu verwenden, rufen Sie `sampleSize()` mit einem Array und einer optionalen Anzahl `n` von Elementen auf, die abgerufen werden sollen. Wenn `n` nicht angegeben wird, gibt die Funktion nur ein zufälliges Element aus dem Array zurück.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
