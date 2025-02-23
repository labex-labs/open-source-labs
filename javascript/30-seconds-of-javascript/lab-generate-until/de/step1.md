# Generieren von Werten bis eine gegebene Bedingung erfüllt ist

Um mit der Code-Praxis zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Nachdem Sie das getan haben, können Sie einen Generator erstellen, der neue Werte produziert, bis eine gegebene Bedingung erfüllt ist.

Um diesen Generator zu erstellen, folgen Sie diesen Schritten:

- Initialisieren Sie den aktuellen `val` mit dem `seed`-Wert.
- Verwenden Sie eine `while`-Schleife, um fortlaufend zu iterieren, solange die `condition`-Funktion, die mit dem aktuellen `val` aufgerufen wird, `false` zurückgibt.
- Verwenden Sie das `yield`-Schlüsselwort, um den aktuellen `val` zurückzugeben und optional einen neuen Seed-Wert, `nextSeed`, zu empfangen.
- Verwenden Sie die `next`-Funktion, um den nächsten Wert aus dem aktuellen `val` und dem `nextSeed` zu berechnen.

Hier ist ein Beispiel-Codeausschnitt:

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Sie können den Generator aufrufen, indem Sie ihn mit den entsprechenden Argumenten aufrufen. Beispielsweise:

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

Dies wird ein Array von Werten von `1` bis `5` erzeugen, da die Bedingung `v > 5` erfüllt ist, wenn `val` gleich `6` ist.
