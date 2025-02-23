# Funktion zum Konvertieren eines Strings in ein Array von Wörtern

Um einen gegebenen String in ein Array von Wörtern zu konvertieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `String.prototype.split()`-Methode mit einem angegebenen `Muster` (Standardmäßig nicht-alphabetisch als Regulärausdruck), um in ein Array von Strings zu konvertieren.
3. Verwenden Sie die `Array.prototype.filter()`-Methode, um alle leeren Strings zu entfernen.
4. Überspringen Sie das zweite Argument, `Muster`, um den Standard-Regulärausdruck zu verwenden.

Hier ist eine Funktion, die diese Schritte implementiert:

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

Sie können die `words()`-Funktion mit verschiedenen Strings verwenden, um sie in Arrays von Wörtern zu konvertieren:

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
