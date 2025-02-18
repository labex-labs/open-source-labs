# 文字列が ISO 形式かどうかをチェックする

与えられた文字列が簡略化拡張 ISO 形式 (ISO 8601) かどうかをチェックするには、以下の手順に従ってください。

1. ターミナル/SSH を開き、`node` と入力してコーディングの練習を開始します。
2. `Date` コンストラクタを使用して、与えられた文字列から `Date` オブジェクトを作成します。
3. `Date.prototype.valueOf()` と `Number.isNaN()` を使用して、生成された日付オブジェクトが有効かどうかをチェックします。
4. `Date.prototype.toISOString()` を使用して、日付の ISO 形式の文字列表現を元の文字列と比較します。
5. 文字列が一致し、日付が有効な場合は `true` を返します。それ以外の場合は `false` を返します。

以下はコードの例です。

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

この関数は、文字列が ISO 形式の場合は `true` を返し、それ以外の場合は `false` を返します。
