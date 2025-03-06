# 特殊ケースの処理

私たちの関数は単純なオブジェクトに対してはうまく動作しますが、より複雑なケースはどうでしょうか？いくつかの特殊ケースを調べ、私たちの関数がそれらをどのように処理するかを見てみましょう。

## 空のオブジェクト

まず、空のオブジェクトでテストしてみましょう。

```javascript
lowerizeKeys({});
```

出力は空のオブジェクトになるはずです。

```
{}
```

## ネストされたオブジェクトを持つオブジェクト

オブジェクトにネストされたオブジェクトが含まれている場合はどうでしょうか？試してみましょう。

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

出力は以下のようになります。

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

最上位のキー `User` のみが小文字に変換され、ネストされたオブジェクト内のキーは変更されていないことに注意してください。

ネストされたオブジェクトを処理するには、すべてのオブジェクトを再帰的に処理するように関数を修正する必要があります。拡張版を作成しましょう。

```javascript
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};
```

この拡張版の関数は以下のように動作します。

1. 各値がオブジェクトであり（配列でも null でもない）、それがネストされたオブジェクトであるかどうかを確認します。
2. もしそうであれば、そのネストされたオブジェクトに対して自身を再帰的に呼び出します。
3. そうでなければ、元の値を使用します。

ネストされたオブジェクトでこれをテストしてみましょう。

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

これで、ネストされたオブジェクト内のすべてのキーも小文字に変換されたことが確認できるはずです。

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

素晴らしい仕事です！ネストされたオブジェクトを処理できる高度な関数を作成しました。
