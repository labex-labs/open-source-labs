# Wie man das letzte Element eines Arrays in JavaScript erhält

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die folgende Funktion gibt das letzte Element in einem Array zurück:

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

Um sie zu verwenden, müssen Sie ein Array als Argument angeben. Die Funktion überprüft, ob das Array wahrheitswertig ist und eine `length`-Eigenschaft hat. Wenn beide Bedingungen wahr sind, berechnet sie den Index des letzten Elements des Arrays und gibt ihn zurück. Andernfalls gibt sie `undefined` zurück.

Hier sind einige Beispiele:

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
