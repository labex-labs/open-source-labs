# Funktion zum Kopieren eines Strings auf die Zwischenablage

Um einen String auf die Zwischenablage zu kopieren, verwenden Sie die `copyToClipboardAsync`-Funktion. Die Funktion gibt ein Promise zurück, das aufgelöst wird, wenn der Inhalt der Zwischenablage aktualisiert wurde. Hier sind die Schritte:

1. Überprüfen Sie, ob die Clipboard API verfügbar ist, indem Sie mithilfe einer `if`-Anweisung überprüfen, ob `Navigator`, `Navigator.clipboard` und `Navigator.clipboard.writeText` wahr sind.
2. Wenn die Clipboard API verfügbar ist, verwenden Sie `Clipboard.writeText()`, um den angegebenen Wert `str` auf die Zwischenablage zu schreiben.
3. Geben Sie das Ergebnis von `Clipboard.writeText()` zurück, das ein Promise ist, das aufgelöst wird, wenn der Inhalt der Zwischenablage aktualisiert wurde.
4. Wenn die Clipboard API nicht verfügbar ist, lehnen Sie das Promise mit einer passenden Fehlermeldung mithilfe von `Promise.reject()` ab.
5. Wenn Sie ältere Browser unterstützen müssen, verwenden Sie `Document.execCommand()` anstelle von `Clipboard.writeText()`. Sie können mehr dazu im Codeausschnitt `copyToClipboard` erfahren.

Hier ist die `copyToClipboardAsync`-Funktion:

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

Um die Funktion zu verwenden, rufen Sie `copyToClipboardAsync` mit dem String auf, den Sie kopieren möchten, als Argument auf, wie folgt:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' kopiert auf die Zwischenablage.
```
