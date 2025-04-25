# プロパティチェッカー

オブジェクトの特定のプロパティが特定の条件を満たすかどうかをチェックするには、`checkProp` 関数を使用します。この関数は、述語関数とプロパティ名を引数として取るカリー化関数を作成します。返された関数は、オブジェクトを取り、指定されたプロパティが述語関数で指定された条件を満たすかどうかに基づいて `true` または `false` を返します。

以下は、`checkProp` の例となる実装です。

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

そして、それを使用する方法のいくつかの例を以下に示します。

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set はサイズを Size として使用し、length ではありません)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

要約すると、`checkProp` 関数を使用することで、特定のプロパティに対する述語関数を指定することで、オブジェクトの特定のプロパティの値を簡単にチェックできます。
