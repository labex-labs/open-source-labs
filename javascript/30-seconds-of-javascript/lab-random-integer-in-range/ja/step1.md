# JavaScriptを使って指定された範囲内で乱数を生成する方法

JavaScriptを使って指定された範囲内で乱数を生成するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. `Math.random()` メソッドを使って0から1の間の乱数を生成します。
3. 生成した乱数に、範囲の最大値と最小値の差を掛け、その結果に最小値を加えることで、目的の範囲にマッピングします。
4. `Math.floor()` メソッドを使って、結果を最も近い整数に切り捨てます。

上記の手順を実装したコードのサンプルは次の通りです。

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

その後、目的の最小値と最大値を使って `randomIntegerInRange()` 関数を呼び出すことで、その範囲内の乱数を生成できます。たとえば：

```js
randomIntegerInRange(0, 5); // 2
```
