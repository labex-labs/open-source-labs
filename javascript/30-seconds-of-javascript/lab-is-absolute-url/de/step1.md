# Funktion zum Überprüfen, ob eine Zeichenfolge eine absolute URL ist

Um zu überprüfen, ob eine gegebene Zeichenfolge eine absolute URL ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codierung zu beginnen.
2. Verwenden Sie `RegExp.prototype.test()`, um zu testen, ob die Zeichenfolge eine absolute URL ist.
3. Die Funktion sollte wie folgt definiert werden: `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4. Die Funktion nimmt ein Zeichenfolgenargument `str` entgegen und gibt `true` zurück, wenn die Zeichenfolge eine absolute URL ist, und `false` andernfalls.
5. Testen Sie die Funktion mit den bereitgestellten Beispielen:

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
