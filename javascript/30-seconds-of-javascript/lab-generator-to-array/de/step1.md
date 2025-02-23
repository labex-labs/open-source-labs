# Konvertieren der Generatorausgabe in ein Array

Um die Ausgabe einer Generatorfunktion in ein Array zu konvertieren, verwenden Sie den Spread-Operator (`...`). Um mit der Codeentwicklung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Beispielfunktion, die einen Generator in ein Array konvertiert:

```js
const generatorToArray = (gen) => [...gen];
```

Sie können diese Funktion wie folgt verwenden:

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
