# オブジェクトのキーにアクセスする

オブジェクトのキーを変換する前に、それらにアクセスする方法を理解する必要があります。JavaScript では `Object.keys()` メソッドが提供されており、これはオブジェクトのすべてのキーを含む配列を返します。

Node.js の対話型シェルで、以下を試してみましょう。

```javascript
Object.keys(user);
```

以下のような出力が表示されるはずです。

```
[ 'Name', 'AGE', 'Email' ]
```

では、`toLowerCase()` メソッドを使用して各キーを小文字に変換してみましょう。`map()` メソッドを使って各キーを変換することができます。

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

出力は以下のようになります。

```
[ 'name', 'age', 'email' ]
```

素晴らしい！すべてのキーが小文字に変換された配列ができました。ただし、これらの小文字のキーと元の値を持つ新しいオブジェクトを作成する必要があります。このために、次のステップで `reduce()` メソッドを使用します。

進む前に `reduce()` メソッドについて理解しましょう。このメソッドは、配列の各要素に対してリデューサー関数を実行し、単一の出力値を返します。

以下は `reduce()` の簡単な例です。

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

出力は `10` になり、これは配列内のすべての数値の合計です。`reduce()` メソッドの `0` はアキュムレーターの初期値です。
