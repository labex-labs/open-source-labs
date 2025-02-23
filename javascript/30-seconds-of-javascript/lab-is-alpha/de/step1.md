# Funktion zum Überprüfen, ob ein String alphabetisch ist

Um zu überprüfen, ob ein String ausschließlich alphabetische Zeichen enthält:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
- Verwenden Sie `RegExp.prototype.test()`, um zu überprüfen, ob die gegebene Zeichenfolge mit dem alphabetischen Regulärausdrucksmuster übereinstimmt.
- Die Funktion `isAlpha` nimmt eine Zeichenfolge als Argument entgegen und gibt `true` zurück, wenn die Zeichenfolge ausschließlich alphabetische Zeichen enthält, und `false` andernfalls.

Hier ist ein Beispiel:

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
