# Wie man den meridiem-Suffix einer Ganzzahl erhält

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion, die eine Ganzzahl in einen String im 12-Stunden-Format mit einem meridiem-Suffix umwandelt.

Um dies zu tun, verwenden Sie den Modulo-Operator (`%`) und bedingte Prüfungen.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Hier sind einige Beispiele für die Verwendung dieser Funktion:

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

Diese Funktion nimmt eine Ganzzahl als Argument entgegen und gibt einen String mit dem meridiem-Suffix zurück.
