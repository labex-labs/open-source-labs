# Luhn-Prüfung

Um den Luhn-Algorithmus zur Validierung von Identifikationsnummern wie Kreditkartennummern, IMEI-Nummern, National Provider Identifier-Nummern zu verwenden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die folgenden Methoden: `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()` und `parseInt()` in Kombination, um ein Array von Ziffern zu erhalten.
3. Verwenden Sie `Array.prototype.shift()`, um die letzte Ziffer zu erhalten.
4. Verwenden Sie `Array.prototype.reduce()`, um den Luhn-Algorithmus zu implementieren.
5. Geben Sie `true` zurück, wenn `sum` durch `10` teilbar ist, andernfalls `false`.

Hier ist der Code:

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

Sie können die Luhn-Prüfungsfunktion mit diesen Beispielen testen:

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
