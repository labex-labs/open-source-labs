# Algorithmus zur Generierung von Zeichenkettenpermutationen

Um alle Permutationen einer Zeichenkette, die Duplikate enthält, zu generieren, verwenden Sie den folgenden Algorithmus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um alle möglichen Permutationen der gegebenen Zeichenkette zu erstellen.
3. Für jeden Buchstaben in der gegebenen Zeichenkette erstellen Sie alle partiellen Permutationen der verbleibenden Buchstaben.
4. Verwenden Sie `Array.prototype.map()`, um den Buchstaben mit jeder partiellen Permutation zu kombinieren.
5. Verwenden Sie `Array.prototype.reduce()`, um alle Permutationen in einem Array zu kombinieren.
6. Die Basisfälle gelten für `String.prototype.length` gleich `2` oder `1`.
7. ⚠️ **WARNUNG**: Die Ausführungszeit steigt exponentiell mit jedem Zeichen. Für Zeichenketten mit mehr als 8 bis 10 Zeichen kann die Umgebung hängen, wenn sie versucht, alle verschiedenen Kombinationen zu lösen.

Hier ist der JavaScript-Code für den Algorithmus:

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

Sie können die `stringPermutations`-Funktion mit dem folgenden Code testen:

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
