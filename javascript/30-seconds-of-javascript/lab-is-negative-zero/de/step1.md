# Prüfen auf negative Null

Um zu prüfen, ob eine Zahl eine negative Null ist, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Verwenden Sie dann folgenden Code:

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

Dieser Code prüft, ob der übergebene Wert gleich `0` ist und ob `1` geteilt durch den Wert gleich `-Infinity` ist. Beispiel:

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
