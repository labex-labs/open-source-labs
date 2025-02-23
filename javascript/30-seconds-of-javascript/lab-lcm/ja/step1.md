# 最小公倍数の計算

2つ以上の数の最小公倍数を計算するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. 最大公約数（GCD）の公式と、`lcm(x, y) = x * y / gcd(x, y)` という事実を使って最小公倍数を求めます。
3. GCDの公式は再帰を使っています。
4. 次のコードをJavaScriptで実装します。

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

使用例:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
