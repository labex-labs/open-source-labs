# JavaScript で再帰を使ってオブジェクトをネストする方法

フラットな配列内のオブジェクトを再帰的にネストするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 相互にリンクされたオブジェクトを再帰を使ってネストします。
3. `id` が `link` と一致する項目をフィルタリングするために `Array.prototype.filter()` を使います。
4. 各項目を新しいオブジェクトにマッピングするために `Array.prototype.map()` を使います。この新しいオブジェクトには `children` プロパティがあり、これは現在の項目の子である項目に基づいて再帰的に項目をネストします。
5. 2 番目の引数 `id` を省略すると、既定で `null` になります。これはオブジェクトが別のオブジェクトにリンクされていないことを示します（つまり、トップレベルのオブジェクトです）。
6. 3 番目の引数 `link` を省略すると、既定のプロパティとして `'parent_id'` が使われます。これにより、オブジェクトがその `id` によって別のオブジェクトにリンクされます。

以下がコードです。

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

`nest()` 関数を使うには、`id` プロパティと `parent_id` プロパティを持つオブジェクトの配列を作成します。この `parent_id` プロパティは、オブジェクトを別のオブジェクトにリンクします。その後、`nest()` 関数を呼び出して、配列を引数として渡します。この関数は、`parent_id` プロパティに基づいてネストされた新しいオブジェクトの配列を返します。

たとえば：

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
