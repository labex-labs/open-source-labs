# Generieren eines zufälligen hexadezimalen Farbcodes in der Konsole/SSH

Um einen zufälligen hexadezimalen Farbcode in der Konsole/SSH zu generieren, folgen Sie den Schritten unten:

1. Öffnen Sie die Konsole/SSH.
2. Geben Sie `node` ein.
3. Verwenden Sie den folgenden Code, um eine zufällige 24-Bit- (6 \* 4 Bits) hexadezimale Zahl zu generieren:

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. Um einen zufälligen hexadezimalen Farbcode zu generieren, rufen Sie die Funktion `randomHexColorCode()` auf.

Beispiel:

```js
randomHexColorCode(); // '#e34155'
```

Dies generiert einen zufälligen hexadezimalen Farbcode, den Sie in Ihren Coding-Projekten verwenden können.
