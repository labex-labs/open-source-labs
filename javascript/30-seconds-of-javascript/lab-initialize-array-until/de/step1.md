# Wie man ein Array initialisiert, bis eine Bedingung erfüllt ist

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier sind die Schritte, um ein Array zu initialisieren und mit Werten zu füllen, die von einer Funktion generiert werden, bis eine bestimmte Bedingung erfüllt ist:

1. Erstellen Sie ein leeres Array `arr`, eine Indexvariable `i` und ein Element `el`.
2. Verwenden Sie eine `do...while`-Schleife, um Elemente mit der `mapFn`-Funktion dem Array hinzuzufügen, bis die `conditionFn`-Funktion für den angegebenen Index `i` und das Element `el` `true` zurückgibt.
3. Die `conditionFn`-Funktion nimmt drei Argumente entgegen: den aktuellen Index, das vorherige Element und das Array selbst.
4. Die `mapFn`-Funktion nimmt drei Argumente entgegen: den aktuellen Index, das aktuelle Element und das Array selbst.

Hier ist der Code:

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

Um die `initializeArrayUntil`-Funktion zu verwenden, geben Sie als Argumente zwei Funktionen an:

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

Dieser Code initialisiert ein Array mit der Fibonacci-Folge bis zur ersten Zahl, die größer als 10 ist. Die `conditionFn`-Funktion überprüft, ob der aktuelle Wert größer als 10 ist, und die `mapFn`-Funktion generiert die nächste Zahl in der Sequenz.
