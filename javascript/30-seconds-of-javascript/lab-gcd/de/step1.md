# Wie man den größten gemeinsamen Teiler berechnet

Um den größten gemeinsamen Teiler zwischen zwei oder mehr Zahlen/Arrays mit Code zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie folgenden Code:

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. Die `gcd`-Funktion verwendet Rekursion.

4. Der Basisfall tritt ein, wenn `y` gleich `0` ist. In diesem Fall gibt die Funktion `x` zurück.

5. Andernfalls gibt die Funktion den größten gemeinsamen Teiler von `y` und dem Rest der Division `x / y` zurück.

6. Um die Funktion zu testen, verwenden Sie folgenden Code:

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
