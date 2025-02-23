# クッキーをシリアライズする方法

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。次に、クッキーの名前と値のペアを Set-Cookie ヘッダー文字列にシリアライズするには、次の手順に従います。

1. 適切な文字列を作成するために、テンプレートリテラルと `encodeURIComponent()` を使用します。
2. `name` と `val` のパラメータを渡して `serializeCookie` 関数を実装します。
3. 関数は適切にシリアライズされた文字列を返します。

`serializeCookie` 関数の使用方法の例を次に示します。

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

この例では、`serializeCookie` 関数はクッキー名として `foo` を受け取り、クッキー値として `bar` を受け取り、`foo=bar` のシリアライズされたクッキー文字列を返します。
