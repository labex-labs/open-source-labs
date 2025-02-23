# Argument Coalescing Factory Code

Um zu beginnen, öffnen Sie Terminal/SSH und geben Sie `node` ein. Diese Funktion gibt das erste Argument zurück, das auf Grundlage des als Argument übergebenen Validators als `true` ausgewertet wird.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Verwenden Sie `Array.prototype.find()`, um das erste Argument zurückzugeben, das von der bereitgestellten Argument-Validierungsfunktion `valid` als `true` zurückgegeben wird. Beispielsweise:

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Hier wird die `coalesceFactory`-Funktion angepasst, um die `customCoalesce`-Funktion zu erstellen. Die `customCoalesce`-Funktion filtert `null`, `undefined`, `NaN` und leere Zeichenketten aus den bereitgestellten Argumenten und gibt das erste Argument zurück, das nicht gefiltert wird. Die Ausgabe von `customCoalesce(undefined, null, NaN, '', 'Waldo')` ist `'Waldo'`.
