# So sortiert man die Zeichen in einer Zeichenkette:

Verwenden Sie den folgenden Code, um die Zeichen in einer Zeichenkette alphabetisch zu sortieren:

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

Beispielverwendung:

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
