# Wie man den Logarithmus in einer bestimmten Basis berechnet

Um den Logarithmus einer gegebenen Zahl in einer bestimmten Basis zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal oder SSH.
2. Tippen Sie `node`, um mit der Code-Praxis zu beginnen.
3. Verwenden Sie den folgenden Code, um den Logarithmus zu berechnen:

```js
const logBase = (n, base) => Math.log(n) / Math.log(base);
```

4. Ersetzen Sie `n` durch die gegebene Zahl und `base` durch die bestimmte Basis.
5. Führen Sie den Code aus, um das Ergebnis zu erhalten.

Hier sind einige Beispiele:

```js
logBase(10, 10); // 1
logBase(100, 10); // 2
```
