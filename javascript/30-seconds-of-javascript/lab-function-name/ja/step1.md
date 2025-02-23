# JavaScript で関数の名前を取得する方法

JavaScript の関数の名前を取得するには、次の手順に従います。

1. ターミナルまたは SSH を開きます。
2. コーディングの練習を始めるために `node` を入力します。
3. `console.debug()` と渡された関数の `name` プロパティを使って、関数の名前をコンソールの `debug` チャネルにログ出力します。
4. 与えられた関数 `fn` を返します。

以下は、JavaScript で関数の名前を取得する方法を示すコード スニペットです。

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// 関数名'max' がコンソールの debug チャネルにログ出力されます。
// m = 6
```

この例では、`functionName` 関数は渡された関数の名前をコンソールの `debug` チャネルにログ出力し、関数自体を返します。関数の `name` プロパティを使ってその名前を取得します。
