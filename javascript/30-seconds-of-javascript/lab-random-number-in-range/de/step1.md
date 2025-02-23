# Wie man in JavaScript eine Zufallszahl in einem bestimmten Bereich generiert

Um in JavaScript eine Zufallszahl in einem bestimmten Bereich zu generieren, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Math.random()`-Methode, um einen Zufallswert zu generieren.
3. Abbilden Sie den generierten Wert auf den gewünschten Bereich mithilfe von Multiplikation.
4. Verwenden Sie den folgenden Code, um eine Funktion zu erstellen, die eine Zufallszahl im angegebenen Bereich generiert:

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5. Um die Funktion zu verwenden, übergeben Sie als Argumente die Mindest- und Höchstwerte des gewünschten Bereichs. Beispielsweise:

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

Indem Sie diese Schritte befolgen, können Sie mit JavaScript leicht eine Zufallszahl in einem angegebenen Bereich generieren.
