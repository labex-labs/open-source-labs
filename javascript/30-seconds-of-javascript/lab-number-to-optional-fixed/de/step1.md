# Konvertieren von Zahlen in die feste Komma-Schreibweise

Um eine Zahl in die feste Komma-Schreibweise ohne Nachkommastellen am Ende zu konvertieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Number.prototype.toFixed()`, um die Zahl in einen String mit fester Komma-Schreibweise zu konvertieren.
3. Verwenden Sie `Number.parseFloat()`, um den String mit fester Komma-Schreibweise wieder in eine Zahl zu konvertieren und dabei die Nachkommastellen am Ende zu entfernen.
4. Verwenden Sie ein Template-Literal, um die Zahl in einen String zu konvertieren.

Beispielcode:

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

Sie können die Funktion mit verschiedenen Eingaben testen:

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
