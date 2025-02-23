# オブジェクトのキーを再帰的にマッピングする

オブジェクトのキーを再帰的にマッピングするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 提供されたオブジェクトと新しいキーを生成する関数を使って `deepMapKeys` 関数を使用します。
3. この関数は、提供されたオブジェクトと同じ値を持ち、各キーに対して提供された関数を実行することで生成されたキーを持つオブジェクトを作成します。
4. `Object.keys()` を使ってオブジェクトのキーを反復処理します。
5. `Array.prototype.reduce()` と提供された関数を使って、同じ値とマッピングされたキーを持つ新しいオブジェクトを作成します。
6. 値がオブジェクトの場合、そのキーもマッピングするために再帰的に `deepMapKeys` を呼び出します。

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

以下は、`deepMapKeys` の使用例です。

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
