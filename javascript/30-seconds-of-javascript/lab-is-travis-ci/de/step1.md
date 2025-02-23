# Überprüfen, ob die Umgebung Travis CI ist

Um zu überprüfen, ob Sie auf Travis CI laufen, verwenden Sie die Funktion `isTravisCI()`. Diese Funktion überprüft, ob die Umgebungsvariablen `TRAVIS` und `CI` vorhanden sind.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Um in Travis CI zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
