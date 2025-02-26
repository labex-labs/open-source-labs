# オブジェクトテーブルビュー

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコンポーネントは、オブジェクトの配列とプロパティ名のリストから動的に作成される行を持つテーブルをレンダリングします。これを達成するには：

- `Object.keys()`、`Array.prototype.filter()`、`Array.prototype.includes()`、および `Array.prototype.reduce()` を使用して、`propertyNames` に指定されたキーを持つすべてのオブジェクトを含む `filteredData` 配列を生成します。
- `propertyNames` の値の数と同じ数の列を持つ `<table>` 要素をレンダリングします。
- `Array.prototype.map()` を使用して、`propertyNames` 配列の各値を `<th>` 要素としてレンダリングします。
- `Array.prototype.map()` を使用して、`filteredData` 配列の各オブジェクトを、オブジェクト内の各キーに対応する `<td>` を含む `<tr>` 要素としてレンダリングします。
- このコンポーネントはネストされたオブジェクトとは動作しません。`propertyNames` に指定されたいずれかのプロパティ内にネストされたオブジェクトがある場合、コンポーネントは破損します。

以下がコードです：

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

オブジェクトの配列とプロパティ名のリストを渡すことでこのコンポーネントを使用できます：

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
