# Überprüfen, ob eine Zahl gerade ist

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Verwenden Sie den folgenden Code, um zu überprüfen, ob eine Zahl gerade oder ungerade ist:

```js
const isEven = (num) => num % 2 === 0;
```

Der obige Code verwendet den Modulo-Operator (`%`), um zu überprüfen, ob eine Zahl ungerade oder gerade ist. Wenn die Zahl gerade ist, gibt die Funktion `true` zurück. Wenn sie ungerade ist, gibt die Funktion `false` zurück.

Hier ist ein Beispiel, wie die `isEven`-Funktion verwendet werden kann:

```js
isEven(3); // gibt false zurück
```
