# Wie man den logischen Nor-Operator in JavaScript verwendet

Um in JavaScript zu beginnen, greifen Sie auf die Konsole/SSH zu und geben Sie `node` ein. Der logische Nor-Operator prüft, ob keine der angegebenen Argumente wahr sind. Um das Gegenteil des logischen Oder von zwei Werten zurückzugeben, verwenden Sie den logischen Nicht-Operator (`!`). Hier ist ein Beispiel:

```js
const nor = (a, b) => !(a || b);
```

Und hier sind einige Ausgaben:

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
