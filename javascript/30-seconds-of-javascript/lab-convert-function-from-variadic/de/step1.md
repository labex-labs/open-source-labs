# Umwandeln einer variadischen Funktion

Um eine variadische Funktion umzuwandeln, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.
2. Erstellen Sie eine Funktion, die eine variadische Funktion annimmt.
3. Verwenden Sie eine Closure und den Spread-Operator (`...`), um das Argumentarray auf die Eingaben der Funktion zuzuordnen.
4. Geben Sie eine neue Funktion zurück, die ein Array von Argumenten akzeptiert und die ursprüngliche variadische Funktion mit diesen Argumenten aufruft.

Hier ist ein Beispiel, wie diese Technik verwendet wird, um die `Math.max`-Funktion umzuwandeln:

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
