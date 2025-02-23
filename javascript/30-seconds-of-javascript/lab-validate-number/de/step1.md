# Zahl-Validierungsfunktion

Um zu überprüfen, ob eine gegebene Eingabe eine Zahl ist, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
- Verwenden Sie `parseFloat()`, um die Eingabe in eine Zahl umzuwandeln.
- Verwenden Sie `Number.isNaN()` und den logischen Negationsoperator (`!`), um zu überprüfen, ob die Eingabe eine Zahl ist.
- Verwenden Sie `Number.isFinite()`, um zu überprüfen, ob die Eingabe endlich ist.
- Verwenden Sie `Number` und den lose Gleichheitsoperator (`==`), um zu überprüfen, ob die Konvertierung stimmt.

Hier ist der Code für die `validateNumber`-Funktion:

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

Sie können die `validateNumber`-Funktion wie folgt verwenden:

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
