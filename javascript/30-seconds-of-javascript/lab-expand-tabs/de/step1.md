# Wie man in JavaScript Tabs in Leerzeichen umwandelt

Um Tab-Zeichen in Leerzeichen umzuwandeln, wenn man codiert, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie die `String.prototype.replace()`-Methode mit einem regulären Ausdruck und `String.prototype.repeat()`, um jedes Tab-Zeichen durch die gewünschte Anzahl von Leerzeichen zu ersetzen.
3. Der folgende Codeausschnitt zeigt, wie die `expandTabs`-Funktion verwendet wird, um Tabs durch Leerzeichen zu ersetzen:

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

Im obigen Beispiel nimmt die `expandTabs`-Funktion zwei Argumente entgegen: einen String `str`, der Tabs enthält, und eine Zahl `count`, die die Anzahl der Leerzeichen angibt, die jedes Tab-Zeichen ersetzen soll. Die Funktion verwendet die `String.prototype.replace()`-Methode mit einem regulären Ausdruck (`/\t/g`), um alle Tab-Zeichen in der Eingabezeichenfolge zu finden und sie mit der gewünschten Anzahl von Leerzeichen mithilfe der `String.prototype.repeat()`-Methode zu ersetzen.
