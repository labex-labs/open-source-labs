# Wie man in JavaScript einen Zufallswert vom Typ Boolean generiert

Um in JavaScript einen Zufallswert vom Typ Boolean zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Methode `Math.random()`, um eine Zufallszahl zu generieren.
3. Überprüfen Sie, ob die Zufallszahl größer oder gleich `0,5` ist.
4. Geben Sie `true` zurück, wenn die Zahl größer oder gleich `0,5` ist, andernfalls geben Sie `false` zurück.

Hier ist eine präzise Implementierung des Codes:

```js
const randomBoolean = () => Math.random() >= 0.5;
```

Sie können die Funktion testen, indem Sie `randomBoolean()` aufrufen, was entweder `true` oder `false` zurückgeben wird.
