# Wie man in JavaScript eine zufällige alphanumerische Zeichenkette generiert

Um in JavaScript eine zufällige Zeichenkette aus alphanumerischen Zeichen zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie ein neues Array mit der angegebenen Länge mithilfe von `Array.from()`.
3. Generieren Sie eine Zufallszahl mit einem Dezimalpunkt mithilfe von `Math.random()`.
4. Konvertieren Sie die Zahl in eine alphanumerische Zeichenkette mithilfe von `Number.prototype.toString()` mit einem `radix`-Wert von `36`.
5. Entfernen Sie den ganzzahligen Teil und den Dezimalpunkt von jeder generierten Zahl mithilfe von `String.prototype.slice()`.
6. Wiederholen Sie diesen Prozess so oft wie erforderlich, bis `length`, mithilfe von `Array.prototype.some()`, da jedes Mal eine Zeichenkette mit variabler Länge erzeugt wird.
7. Schneiden Sie die generierte Zeichenkette ab, wenn sie länger als die gegebene `length` ist, mithilfe von `String.prototype.slice()`.
8. Geben Sie die generierte Zeichenkette zurück.

Hier ist der Code:

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

Sie können die `randomAlphaNumeric()`-Funktion mit der gewünschten Länge als Argument aufrufen. Beispiel:

```js
randomAlphaNumeric(5); // '0afad'
```
