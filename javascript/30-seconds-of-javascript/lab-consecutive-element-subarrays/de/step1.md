# Subarrays aus aufeinanderfolgenden Elementen

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Der folgende Code erstellt ein Array von n-Tupeln aus aufeinanderfolgenden Elementen.

```js
const aperture = (n, arr) =>
  n > arr.length ? [] : arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Um die Funktion zu verwenden:

- Rufen Sie die Funktion `aperture(n, arr)` mit `n` als Anzahl der aufeinanderfolgenden Elemente und `arr` als Array von Zahlen auf.
- Die Funktion gibt ein Array von n-Tupeln aus aufeinanderfolgenden Elementen aus `arr` zurück.
- Wenn `n` größer als die Länge von `arr` ist, gibt die Funktion ein leeres Array zurück.

Beispielverwendung:

```js
aperture(2, [1, 2, 3, 4]); // [[1, 2], [2, 3], [3, 4]]
aperture(3, [1, 2, 3, 4]); // [[1, 2, 3], [2, 3, 4]]
aperture(5, [1, 2, 3, 4]); // []
```
