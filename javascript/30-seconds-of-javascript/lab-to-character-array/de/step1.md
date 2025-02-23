# Wie man in JavaScript eine Zeichenfolge in ein Array von Zeichen umwandelt

Um in JavaScript eine Zeichenfolge in ein Array von Zeichen umzuwandeln, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den Spread-Operator (`...`), um die Zeichenfolge in ein Array von Zeichen umzuwandeln.
3. Definieren Sie eine Funktion namens `toCharArray`, die eine Zeichenfolge als Argument nimmt und ein Array ihrer Zeichen zurückgibt.
4. Rufen Sie die `toCharArray`-Funktion mit der Zeichenfolge auf, die Sie umwandeln möchten, als Argument.
5. Die Funktion wird ein Array von Zeichen zurückgeben.

Hier ist der Code:

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
