# Funktion zum Ersetzen des letzten Vorkommens eines Musters in einer Zeichenkette

Hier ist eine Funktion, die das letzte Vorkommen eines Musters in einer Zeichenkette ersetzt:

```js
const replaceLast = (str, pattern, replacement) => {
```

Um sie zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

- Verwenden Sie zunächst `typeof`, um festzustellen, ob `pattern` eine Zeichenkette oder ein regulärer Ausdruck (regular expression) ist.
- Wenn `pattern` eine Zeichenkette ist, verwenden Sie sie als `match`.
- Andernfalls verwenden Sie den `RegExp`-Konstruktor, um einen neuen regulären Ausdruck zu erstellen, indem Sie die `RegExp.prototype.source` von `pattern` verwenden und das `'g'`-Flag hinzufügen. Verwenden Sie `String.prototype.match()` und `Array.prototype.slice()`, um das letzte Vorkommen (falls vorhanden) zu erhalten.

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- Verwenden Sie `String.prototype.lastIndexOf()`, um das letzte Vorkommen des Treffers in der Zeichenkette zu finden.
- Wenn ein Treffer gefunden wird, verwenden Sie `String.prototype.slice()` und ein Template-Literal, um das übereinstimmende Teilzeichenkette durch die angegebene `replacement` zu ersetzen.
- Wenn kein Treffer gefunden wird, geben Sie die ursprüngliche Zeichenkette zurück.

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

Hier sind einige Beispiele, wie Sie die Funktion verwenden können:

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
