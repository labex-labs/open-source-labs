# Wie man den Namen einer Funktion in JavaScript erhält

Um den Namen einer JavaScript-Funktion zu erhalten, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal oder SSH.
2. Geben Sie `node` ein, um mit der Codeausführung zu beginnen.
3. Verwenden Sie `console.debug()` und die `name`-Eigenschaft der übergebenen Funktion, um den Funktionsnamen in den `debug`-Kanal der Konsole auszugeben.
4. Geben Sie die gegebene Funktion `fn` zurück.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie man den Namen einer Funktion in JavaScript erhält:

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// Der Funktionsname'max' wird im debug-Kanal der Konsole ausgegeben.
// m = 6
```

In diesem Beispiel gibt die `functionName`-Funktion den Namen der übergebenen Funktion in den `debug`-Kanal der Konsole aus und gibt die Funktion selbst zurück. Die `name`-Eigenschaft der Funktion wird verwendet, um ihren Namen zu erhalten.
