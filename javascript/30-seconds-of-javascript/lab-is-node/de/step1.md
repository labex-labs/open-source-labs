# Wie man feststellt, ob die aktuelle Laufzeitumgebung Node.js ist

Um festzustellen, ob die aktuelle Laufzeitumgebung Node.js ist, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein.
3. Verwenden Sie das globale Objekt `process`, das Informationen über den aktuellen Node.js-Prozess liefert.
4. Überprüfen Sie, ob `process`, `process.versions` und `process.versions.node` definiert sind.

Hier ist der Code, um festzustellen, ob die aktuelle Laufzeitumgebung Node.js ist:

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

Sie können den Code testen, indem Sie die `isNode`-Funktion aufrufen:

```js
isNode(); // true (Node)
isNode(); // false (Browser)
```
