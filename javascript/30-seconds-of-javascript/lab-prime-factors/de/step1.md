# Wie man mit dem Versuchsdurchdivision-Algorithmus die Primfaktoren einer Zahl findet

Um mit dem Versuchsdurchdivision-Algorithmus die Primfaktoren einer gegebenen Zahl zu finden, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie eine `while-Schleife`, um über alle möglichen Primfaktoren zu iterieren, beginnend mit `2`.
- Wenn der aktuelle Faktor, `f`, die Zahl `n` exakt teilt, fügen Sie `f` dem Array `factors` hinzu und dividieren Sie `n` durch `f`. Andernfalls erhöhen Sie `f` um eins.
- Die Funktion `primeFactors` nimmt eine Zahl `n` als Eingabe und gibt ein Array ihrer Primfaktoren zurück.
- Um die Funktion zu testen, rufen Sie `primeFactors(147)` auf, und es wird `[3, 7, 7]` zurückgeben.

Hier ist der JavaScript-Code:

```js
const primeFactors = (n) => {
  let a = [],
    f = 2;
  while (n > 1) {
    if (n % f === 0) {
      a.push(f);
      n /= f;
    } else {
      f++;
    }
  }
  return a;
};
```

Denken Sie daran, `147` durch die Zahl zu ersetzen, von der Sie die Primfaktoren finden möchten.
