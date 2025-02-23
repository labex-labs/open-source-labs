# Wie man HTML/XML-Tags aus einem String entfernt

Um HTML/XML-Tags aus einem String zu entfernen, kann man eine reguläre Ausdruck verwenden. Folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH
2. Tippen Sie `node`, um mit der Code-Praxis zu beginnen
3. Verwenden Sie den folgenden Code:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Testen Sie die Funktion mit dem folgenden Beispiel:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

Dies entfernt alle HTML/XML-Tags aus dem Eingabestring und gibt den verbleibenden Text zurück.
