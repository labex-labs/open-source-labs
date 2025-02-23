# Überprüfen, ob eine Zahl eine Zweierpotenz ist

Um zu überprüfen, ob eine Zahl eine Zweierpotenz ist, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den bitweisen binären UND-Operator (`&`), um zu bestimmen, ob die Zahl (`n`) eine Zweierpotenz ist.
3. Überprüfen Sie zusätzlich, dass `n` nicht falsch ist.
4. Der folgende Code überprüft funktionell, ob `n` eine Zweierpotenz ist:

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

Hier sind einige Beispiele für die Verwendung der `isPowerOfTwo`-Funktion:

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
