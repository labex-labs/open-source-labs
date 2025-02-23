# 配列を2つのグループに分割する関数

この関数を使って値に基づいて配列を2つのグループに分割するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. 与えられた `filter` 配列の結果に基づいて値を2つのグループに分割する `bifurcate()` 関数を使います。
3. 関数を実装するには、`filter` 配列に基づいてグループに要素を追加するために `Array.prototype.reduce()` と `Array.prototype.push()` を使います。
4. `filter` がどの要素に対しても真値を持つ場合は、それを最初のグループに追加します。それ以外の場合は、2番目のグループに追加します。

以下は `bifurcate()` 関数のコードです。

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

値の配列と対応するフィルタ配列を使って `bifurcate()` 関数を呼び出すことで、値を2つのグループに分割できます。たとえば：

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
