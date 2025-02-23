# Wie man im Terminal/SSH mit Programmieren beginnt

Um im Terminal/SSH mit Programmieren zu beginnen, tippe einfach `node`.

# Ein mehrzeiliges String in ein Array von Zeilen aufteilen

Um einen mehrzeiligen String in ein Array von Zeilen aufzuteilen:

- Verwende `String.prototype.split()` und eine reguläre Ausdrucksmuster, um Zeilenumbrüche zu finden und ein Array zu erstellen.
- Das reguläre Ausdrucksmuster `/\r?\n/` findet sowohl `\r` als auch `\n` Zeilenumbrüche.
- Dies wird ein Array von Zeilen zurückgeben.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a','multiline','string.', '']
```
