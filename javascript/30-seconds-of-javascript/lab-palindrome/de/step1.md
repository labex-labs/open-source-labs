# Wie überprüft man in JavaScript, ob ein String ein Palindrom ist?

Um zu überprüfen, ob ein gegebener String in JavaScript ein Palindrom ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Normalisieren Sie den String in Kleinbuchstaben mit der `String.prototype.toLowerCase()`-Methode.
3. Entfernen Sie nicht-alphanumerische Zeichen aus dem String mit der `String.prototype.replace()`-Methode und einem regulären Ausdruck `[\W_]`.
4. Teilen Sie den normalisierten String in einzelne Zeichen auf, indem Sie den Spread-Operator (`...`) verwenden.
5. Kehren Sie die Zeichenfolge um, indem Sie die `Array.prototype.reverse()`-Methode verwenden.
6. Verbinden Sie die umgekehrte Zeichenfolge zu einem String mit der `Array.prototype.join()`-Methode.
7. Vergleichen Sie die umgekehrte Zeichenfolge mit der normalisierten Zeichenfolge, um zu bestimmen, ob es sich um ein Palindrom handelt.

Hier ist ein Beispielcodeausschnitt, der die obigen Schritte implementiert:

```js
const palindrome = (str) => {
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, "");
  return normalizedStr === [...normalizedStr].reverse().join("");
};

console.log(palindrome("taco cat")); // true
```

Im obigen Beispiel nimmt die `palindrome()`-Funktion einen String-Argument entgegen und gibt `true` zurück, wenn der String ein Palindrom ist, und `false` andernfalls. Die Funktion verwendet die oben beschriebenen Schritte, um zu überprüfen, ob der String ein Palindrom ist.
