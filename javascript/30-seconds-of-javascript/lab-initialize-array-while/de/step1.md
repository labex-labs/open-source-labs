# Wie man ein Array in JavaScript mit einer While-Schleife initialisiert und füllt

Um zu beginnen, JavaScript zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `initializeArrayWhile`-Funktion initialisiert und füllt ein Array mit Werten, die von einer Funktion generiert werden, solange eine Bedingung erfüllt ist. So funktioniert es:

1. Erstellen Sie ein leeres Array namens `arr`, eine Indexvariable namens `i` und ein Element namens `el`.
2. Verwenden Sie eine `while`-Schleife, um Elemente mit der `mapFn`-Funktion dem Array hinzuzufügen, solange die `conditionFn`-Funktion für den gegebenen Index `i` und das Element `el` `true` zurückgibt.
3. Die `conditionFn`-Funktion nimmt drei Argumente entgegen: den aktuellen Index, das vorherige Element und das Array selbst.
4. Die `mapFn`-Funktion nimmt drei Argumente entgegen: den aktuellen Index, das aktuelle Element und das Array selbst.
5. Die `initializeArrayWhile`-Funktion gibt das Array zurück.

Hier ist der Code:

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

Sie können die `initializeArrayWhile`-Funktion verwenden, um ein Array mit Werten zu initialisieren und zu füllen. Beispielsweise:

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
