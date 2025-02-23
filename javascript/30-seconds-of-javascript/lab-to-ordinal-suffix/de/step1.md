# Funktion zur Umwandlung von Zahlen in die Endung für die Ordnungszahl

Um eine Zahl in die Endung für die Ordnungszahl umzuwandeln, verwenden Sie die `toOrdinalSuffix`-Funktion.

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Die Funktion nimmt eine Zahl als Eingabe entgegen und gibt sie als Zeichenfolge mit der korrekten Endung für die Ordnungszahl zurück.
- Verwenden Sie den Modulo-Operator (`%`), um die Werte der Einer- und Zehnerstellen zu finden.
- Finden Sie heraus, welche Ziffern des Ordnungsmusters übereinstimmen.
- Wenn die Ziffer im Teens-Pattern gefunden wird, verwenden Sie die Endung für die Teens-Zahlen.

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

Hier ist ein Beispiel für die Verwendung der `toOrdinalSuffix`-Funktion:

```js
toOrdinalSuffix("123"); // '123rd'
```
