# Wie man Fahrenheit in Celsius umrechnet, mit NodeJS

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Anschließend folgen Sie diesen Schritten, um Fahrenheit in Celsius umzurechnen:

1. Verwenden Sie die Umrechnungsformel `C = (F - 32) * 5 / 9`.
2. Erstellen Sie in NodeJS eine Funktion, um die Formel anzuwenden:

```js
const fahrenheitToCelsius = (degrees) => ((degrees - 32) * 5) / 9;
```

3. Testen Sie die Funktion, indem Sie einen Fahrenheit-Grad als Argument eingeben:

```js
fahrenheitToCelsius(32); // 0
```

Indem Sie diese Schritte befolgen, können Sie Temperaturen von Fahrenheit in Celsius mit NodeJS leicht umrechnen.
