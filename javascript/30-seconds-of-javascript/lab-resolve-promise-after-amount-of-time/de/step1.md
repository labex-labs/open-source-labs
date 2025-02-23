# Ein Promise mit Verzögerung erstellen

Um ein neues Promise zu erstellen, das nach einer bestimmten Zeit aufgelöst wird, folgen Sie diesen Schritten:

1. Verwenden Sie den `Promise`-Konstruktor, um ein neues Promise zu erstellen.
2. Innerhalb der Ausführungsfunktion des Promises verwenden Sie `setTimeout()`, um die `resolve`-Funktion des Promises mit dem bereitgestellten `value` nach der angegebenen `delay` aufzurufen.

Hier ist eine Beispielimplementierung von `resolveAfter()`:

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

Jetzt können Sie `resolveAfter()` aufrufen, um ein Promise zu erhalten, das nach der angegebenen Verzögerung auf den bereitgestellten Wert aufgelöst wird:

```js
resolveAfter("Hello", 1000);
// Gibt ein Promise zurück, das nach 1s auf 'Hello' aufgelöst wird
```

Um mit der Code-Praxis zu beginnen, öffnen Sie das Terminal oder SSH und geben Sie `node` ein.
