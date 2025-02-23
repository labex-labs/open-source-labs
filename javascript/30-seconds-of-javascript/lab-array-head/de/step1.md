# Wie man das erste Element eines Arrays in JavaScript bekommt

Um das erste Element eines Arrays in JavaScript zu erhalten, kannst du die `head`-Funktion verwenden. Hier ist, wie du sie verwenden kannst:

1. Öffne das Terminal/SSH.
2. Tippe `node`, um mit der Codeausführung zu beginnen.
3. Verwende den folgenden Code, um das erste Element eines Arrays zu erhalten:

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. Rufe die `head`-Funktion mit einem Array als Argument auf, um das erste Element zu erhalten. Wenn das Array leer oder falsch ist, wird die Funktion `undefined` zurückgeben.

Hier sind einige Beispiele:

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
