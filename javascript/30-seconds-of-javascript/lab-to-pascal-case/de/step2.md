# Arbeiten mit regulären Ausdrücken (Regular Expressions) zum Aufteilen von Wörtern

Um einen String in Pascal Case umzuwandeln, ist der erste Schritt, den String in einzelne Wörter aufzuteilen. Wir können reguläre Ausdrücke (Regex) verwenden, um Wortgrenzen zu identifizieren, unabhängig davon, welches Trennzeichen verwendet wird (Leerzeichen, Bindestriche, Unterstriche usw.).

In JavaScript werden reguläre Ausdrücke zwischen Schrägstrichen (`/Muster/`) eingeschlossen. Lassen Sie uns untersuchen, wie man Regex verwendet, um einen String in Wörter aufzuteilen.

1. In Ihrer Node.js-Sitzung probieren wir zunächst ein einfaches Beispiel. Geben Sie den folgenden Code ein:

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

Die Ausgabe sollte sein:

```
[ 'hello', 'world', 'example' ]
```

Dieser Regex `/[-_]/` passt entweder auf einen Bindestrich oder einen Unterstrich, und `split()` verwendet diese Übereinstimmungen als Trennzeichen.

2. Jetzt probieren wir einen komplexeren String und einen komplexeren Regex. Geben Sie ein:

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

Die Ausgabe sollte sein:

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

Lassen Sie uns diesen Regex zerlegen:

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`: Passt auf Sequenzen von Großbuchstaben
- `/[A-Z]?[a-z]+[0-9]*/`: Passt auf Wörter, die mit einem Großbuchstaben beginnen können
- `/[A-Z]/`: Passt auf einzelne Großbuchstaben
- `/[0-9]+/`: Passt auf Zahlenfolgen
- Das `g`-Flag macht die Übereinstimmung global (findet alle Übereinstimmungen)

Die `match()`-Methode gibt ein Array aller im String gefundenen Übereinstimmungen zurück. Dies wird für unseren Pascal-Case-Konverter unerlässlich sein, da es Wörter in fast jedem Format identifizieren kann.
