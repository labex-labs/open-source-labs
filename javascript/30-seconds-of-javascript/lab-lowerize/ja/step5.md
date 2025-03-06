# 再利用可能なモジュールの作成

動作する関数ができたので、他のプロジェクトにインポートできる再利用可能な JavaScript モジュールファイルを作成しましょう。

まず、Ctrl+C を 2 回押すか、`.exit` と入力して Enter キーを押して、Node.js の対話型シェルを終了します。

次に、プロジェクトディレクトリに `object-utils.js` という名前の新しいファイルを作成します。

1. WebIDE で、左側のファイルエクスプローラーパネルに移動します。
2. プロジェクトディレクトリ内で右クリックし、「New File」を選択します。
3. ファイル名を `object-utils.js` とします。
4. 以下のコードをファイルに追加します。

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
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

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

次に、モジュールが正しく動作することを確認するためのテストファイルを作成しましょう。`test.js` という名前の新しいファイルを作成します。

1. WebIDE で、左側のファイルエクスプローラーパネルに移動します。
2. プロジェクトディレクトリ内で右クリックし、「New File」を選択します。
3. ファイル名を `test.js` とします。
4. 以下のコードをファイルに追加します。

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

では、テストファイルを実行しましょう。

```bash
node test.js
```

以下のような出力が表示されるはずです。

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

おめでとうございます！オブジェクトのキーを小文字に変換する関数を持つ再利用可能な JavaScript モジュールを成功させて作成しました。このモジュールは、あなたの JavaScript プロジェクトにインポートできます。
