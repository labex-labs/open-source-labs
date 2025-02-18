# Umwandlung einer Ganzzahl in römische Numerale

Um eine Ganzzahl in ihre römische Numeral-Darstellung umzuwandeln, befolgen Sie diese Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codierung zu beginnen.

2. Die Funktion `toRomanNumeral()` akzeptiert Werte zwischen `1` und `3999` (beide inklusive).

3. Erstellen Sie eine Nachschlagetabelle (Lookup-Tabelle), die Arrays mit zwei Werten in der Form (römischer Wert, Ganzzahl) enthält.

4. Verwenden Sie `Array.prototype.reduce()`, um über die Werte in `lookup` zu iterieren und `num` wiederholt durch den Wert zu teilen.

5. Verwenden Sie `String.prototype.repeat()`, um die römische Numeral-Darstellung zum Akkumulator hinzuzufügen.

Hier ist der Code für die Funktion `toRomanNumeral()`:

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

Sie können die Funktion mit diesen Beispielen testen:

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
