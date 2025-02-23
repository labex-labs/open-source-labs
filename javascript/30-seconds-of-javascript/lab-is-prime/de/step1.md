# Funktion, um zu überprüfen, ob eine Zahl eine Primzahl ist

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion überprüft, ob eine gegebene Ganzzahl eine Primzahl ist. Hier sind die Schritte, um zu überprüfen, ob eine Zahl eine Primzahl ist:

1. Überprüfen Sie die Zahlen von `2` bis zur Quadratwurzel der gegebenen Zahl.
2. Wenn eine von ihnen die gegebene Zahl teilt, geben Sie `false` zurück.
3. Wenn keine von ihnen die gegebene Zahl teilt, geben Sie `true` zurück, es sei denn, die Zahl ist kleiner als `2`.

Hier ist der Code, um diese Funktion in JavaScript zu implementieren:

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

Sie können die Funktion testen, indem Sie sie mit einer Zahl als Argument aufrufen:

```js
isPrime(11); // true
```
