# Überprüfen, ob ein String gültiges JSON ist

Um zu überprüfen, ob ein gegebener String gültiges JSON ist, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `JSON.parse()`-Methode und einen `try...catch`-Block, um zu überprüfen, ob der bereitgestellte String gültiges JSON ist.
3. Wenn der String gültig ist, geben Sie `true` zurück. Andernfalls geben Sie `false` zurück.

Hier ist ein Beispielcodeausschnitt, der diese Logik implementiert:

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

Sie können diese Funktion mit verschiedenen Eingabestrings testen, wie folgt:

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

Im letzten Beispiel ist `null` kein gültiger JSON-String, daher gibt die Funktion `false` zurück.
