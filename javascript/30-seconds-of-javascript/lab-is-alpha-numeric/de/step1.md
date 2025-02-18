# Prüfen, ob eine Zeichenkette alphanumerisch ist

Wenn Sie das Programmieren üben möchten, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Hier ist eine Funktion, die prüft, ob eine Zeichenkette nur alphanumerische Zeichen enthält:

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

Um sie zu verwenden, rufen Sie `isAlphaNumeric` mit einer Zeichenkette als Argument auf. Sie gibt `true` zurück, wenn die Zeichenkette nur alphanumerische Zeichen enthält, und `false` sonst.

Beispiel:

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false (enthält ein Leerzeichen)
isAlphaNumeric("#$hello"); // false (enthält nicht-alphanumerische Zeichen)
```

Die Methode `RegExp.prototype.test()` wird verwendet, um zu prüfen, ob die Eingabezeichenkette mit dem alphanumerischen Muster übereinstimmt, das durch den regulären Ausdruck `/^[a-z0-9]+$/gi` dargestellt wird. Dieses Muster passt auf jede Sequenz von einem oder mehreren Kleinbuchstaben oder Ziffern, und die Flags `g` und `i` machen die Übereinstimmung gross- und kleinschreibungsunabhängig.
