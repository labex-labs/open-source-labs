# オブジェクトを展開する関数

配列値のプロパティによってオブジェクトを展開するには、`unwind` 関数を使用します。

- コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。
- この関数は、オブジェクト分解構文を使用して、指定された `key` に対するキーバリューペアをオブジェクトから除外します。
- 次に、与えられた `key` の値に対して `Array.prototype.map()` を使用して、オブジェクトの配列を作成します。
- 各オブジェクトは、元のオブジェクトの値を含みますが、`key` は個々の値にマップされます。

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

使用例：

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
