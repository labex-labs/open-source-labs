# JavaScript で値を配列に変換する

値を配列に変換するには、以下に示す `castArray` 関数を使用します。

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

この関数を使用するには、変換したい値を引数として渡します。関数は `Array.isArray()` を使用して値が既に配列であるかどうかを確認します。配列である場合は、関数はそのまま返します。配列でない場合は、関数は配列にカプセル化された値を返します。

以下は、`castArray` を使用する方法の例です。

```js
castArray("foo"); // 返す値: ['foo']
castArray([1]); // 返す値: [1]
```

JavaScript でコーディングを練習するには、ターミナルまたは SSH を開き、`node` と入力します。
