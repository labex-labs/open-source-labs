# Wie man nicht-ASCII-Zeichen in JavaScript entfernt

Um nicht druckbare ASCII-Zeichen in JavaScript zu entfernen, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codierung zu beginnen.
2. Verwenden Sie die Methode `String.prototype.replace()` mit einem regulären Ausdruck, um nicht druckbare ASCII-Zeichen zu entfernen.
3. Der reguläre Ausdruck `/[^\x20-\x7E]/g` findet jedes Zeichen, das nicht im druckbaren ASCII-Bereich liegt (Dezimalwerte 32 bis 126).
4. Das `g`-Flag wird verwendet, um eine globale Suche durchzuführen (d. h., alle Vorkommen von nicht-ASCII-Zeichen im String zu ersetzen).
5. Hier ist ein Beispiel, wie Sie die Funktion `removeNonASCII` verwenden können:

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

Dies wird den String zurückgeben, in dem alle nicht-ASCII-Zeichen entfernt wurden.
