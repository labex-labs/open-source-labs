# 小文字変換関数の作成

オブジェクトのキーにアクセスする方法と `reduce()` メソッドの使い方がわかったので、オブジェクトのすべてのキーを小文字に変換する関数を作成しましょう。

Node.js の対話型シェルで、以下の関数を定義します。

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

この関数が何をするかを分解してみましょう。

1. `Object.keys(obj)` は入力オブジェクトのすべてのキーを取得します。
2. `.reduce()` はこれらのキーを新しいオブジェクトに変換します。
3. 各キーについて、アキュムレーターオブジェクト (`acc`) に新しいエントリを作成します。
   - `key.toLowerCase()` を使ってキーを小文字に変換します。
   - 入力オブジェクトから元の値 (`obj[key]`) を取得します。
4. アキュムレーターの初期値として空のオブジェクト `{}` から始めます。
5. 最後に、アキュムレーターを返します。これが小文字のキーを持つ新しいオブジェクトです。

では、先ほど作成した `user` オブジェクトでこの関数をテストしてみましょう。

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

以下の出力が表示されるはずです。

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

完璧です！すべてのキーが小文字になりました。

この関数が正しく動作することを確認するために、別の例を試してみましょう。

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

出力は以下のようになるはずです。

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

この関数は、さまざまなキーの大文字小文字スタイルを持つ異なるオブジェクトに対して正しく動作します。
