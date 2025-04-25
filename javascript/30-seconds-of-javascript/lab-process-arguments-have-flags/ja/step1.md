# プロセス引数にフラグが含まれているかどうかを確認する

現在のプロセスの引数に指定されたフラグが含まれているかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. `Array.prototype.every()`と`Array.prototype.includes()`を使って、`process.argv`に指定されたすべてのフラグが含まれているかどうかを確認します。
3. 正規表現を使って、指定されたフラグが`-`または`--`で始まっているかどうかをテストし、それに応じて接頭辞を付けます。

これを実装する方法を示すコードスニペットは次のとおりです。

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

この関数を次のように異なるフラグでテストすることができます。

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
