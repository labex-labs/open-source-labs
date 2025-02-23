# Überprüfen, ob Prozessargumente Flags enthalten

Um zu überprüfen, ob die Argumente des aktuellen Prozesses bestimmte Flags enthalten, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.every()` und `Array.prototype.includes()`, um zu überprüfen, ob `process.argv` alle angegebenen Flags enthält.
3. Verwenden Sie eine reguläre Ausdruck, um zu testen, ob die angegebenen Flags mit `-` oder `--` präfixiert sind, und prefixieren Sie sie entsprechend.

Hier ist ein Codeausschnitt, der zeigt, wie dies implementiert werden kann:

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

Sie können die Funktion mit verschiedenen Flags wie folgt testen:

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
