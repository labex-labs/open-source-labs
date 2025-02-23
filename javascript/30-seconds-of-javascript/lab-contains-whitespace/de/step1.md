# Prüfen auf Leerzeichen in einem String

Um zu überprüfen, ob ein String Leerzeichen enthält, folgen Sie den Schritten unten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
- Verwenden Sie `RegExp.prototype.test()` mit einem passenden regulären Ausdruck, um zu überprüfen, ob der gegebene String Leerzeichen enthält.
- Hier ist ein Beispielcodeausschnitt:

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- Um die Funktion zu testen, rufen Sie `containsWhitespace` mit einem String als Argument auf. Sie wird `true` zurückgeben, wenn der String Leerzeichen enthält, andernfalls `false`.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
