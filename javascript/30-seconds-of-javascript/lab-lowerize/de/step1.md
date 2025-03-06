# Grundlagen zu Objekten in JavaScript

Bevor wir beginnen, die Schlüssel (keys) von Objekten in Kleinbuchstaben umzuwandeln, lernen wir zunächst, was JavaScript-Objekte sind und wie wir mit ihnen arbeiten können.

In JavaScript ist ein Objekt eine Sammlung von Schlüssel-Wert-Paaren (key-value pairs). Die Schlüssel (keys) sind Strings (oder Symbole), und die Werte können von jedem Datentyp sein, einschließlich anderer Objekte.

Beginnen wir damit, die Node.js interaktive Shell zu öffnen:

1. Öffnen Sie das Terminal in Ihrer WebIDE.
2. Geben Sie `node` ein und drücken Sie die Eingabetaste.

Sie sollten jetzt die Node.js-Eingabeaufforderung (`>`) sehen, die es Ihnen ermöglicht, direkt JavaScript-Code einzugeben.

Erstellen wir ein einfaches Objekt mit Schlüsseln in gemischter Groß- und Kleinschreibung:

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Geben Sie diesen Code in die Node.js-Eingabeaufforderung ein und drücken Sie die Eingabetaste. Um das Objekt anzuzeigen, geben Sie einfach `user` ein und drücken Sie die Eingabetaste:

```javascript
user;
```

Sie sollten die folgende Ausgabe sehen:

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

Wie Sie sehen können, hat dieses Objekt Schlüssel (keys) mit unterschiedlichen Groß- und Kleinschreibungen. Im nächsten Schritt lernen wir, wie wir auf diese Schlüssel zugreifen und sie in Kleinbuchstaben umwandeln können.
