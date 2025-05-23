# Unix タイムスタンプから Date オブジェクトを作成する方法

Unix タイムスタンプから`Date`オブジェクトを作成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. タイムスタンプに`1000`を掛けてミリ秒に変換します。
3. `Date`コンストラクタを使用して新しい`Date`オブジェクトを作成します。

以下はコードの例です。

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

この関数を使って、Unix タイムスタンプを`Date`オブジェクトに変換することができます。

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
