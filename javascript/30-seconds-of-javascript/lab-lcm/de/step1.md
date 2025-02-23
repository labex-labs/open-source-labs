# Das kleinste gemeinsame Vielfache berechnen

Um das kleinste gemeinsame Vielfache von zwei oder mehr Zahlen zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie die Formel für den größten gemeinsamen Teiler (GCD) und die Tatsache, dass `kgV(x, y) = x * y / ggT(x, y)`, um das kleinste gemeinsame Vielfache zu bestimmen.
3. Die GCD-Formel verwendet Rekursion.
4. Implementieren Sie den folgenden Code in JavaScript:

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

Beispielverwendung:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
