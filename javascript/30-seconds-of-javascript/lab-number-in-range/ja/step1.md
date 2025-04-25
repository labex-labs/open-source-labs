# 与えられた範囲内に数値があるかどうかをチェックする関数

数値が指定された範囲内にあるかどうかをチェックするには、`inRange`関数を使用します。まず、ターミナル/SSH を開き、コーディングを開始するために`node`と入力します。

`inRange`関数を使用する手順は以下の通りです。

1. 与えられた数値が指定された範囲内にあるかどうかを算術比較を使ってチェックします。
2. 2 番目の引数`end`が指定されていない場合、範囲は`0`から`start`までと見なされます。
3. `inRange`関数は 3 つの引数`n`、`start`、および`end`を取ります。
4. `end`が`start`より小さい場合、関数は`start`と`end`の値を交換します。
5. `end`が指定されていない場合、関数は`n`が 0 以上で`start`未満であるかどうかをチェックします。
6. `end`が指定されている場合、関数は`n`が`start`以上で`end`未満であるかどうかをチェックします。
7. 関数は`n`が指定された範囲内にある場合に`true`を返し、それ以外の場合は`false`を返します。

以下が`inRange`関数です。

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

`inRange`関数の使い方の例をいくつか示します。

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
